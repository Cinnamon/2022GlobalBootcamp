import os
import pickle
import datetime

import torch
import librosa
import numpy as np 
import gradio as gr
from gtts import gTTS
from PIL import Image
from torchvision import transforms

from build_vocab import Vocabulary
from model import EncoderStory, DecoderStory
from utils import hconcat_resize, transform_image


def get_model():
    encoder_path = './models/encoder-0.pkl'
    decoder_path = './models/decoder-0.pkl'
    vocab_path = './models/vocab.pkl'

    img_feature_size = 1024
    embed_size = 256
    hidden_size = 1024
    num_layers = 2

    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)

    encoder = EncoderStory(img_feature_size, hidden_size, num_layers)
    decoder = DecoderStory(embed_size, hidden_size, vocab)

    encoder.load_state_dict(torch.load(encoder_path))
    decoder.load_state_dict(torch.load(decoder_path))

    encoder.eval()
    decoder.eval()

    if torch.cuda.is_available():
        encoder.cuda()
        decoder.cuda()
    
    return encoder, decoder, vocab


# load the models only once
encoder, decoder, vocab = get_model()


def generate_story(images):
    transform = transforms.Compose([
            transforms.ToTensor(), 
            transforms.Normalize((0.485, 0.456, 0.406), 
                      (0.229, 0.224, 0.225))])
    
    image_tensor = []
    for image in images:
        image = transform_image(image, transform)
        image_tensor.append(image)

    image_tensor = torch.stack(image_tensor).squeeze(1).unsqueeze(0)
    if torch.cuda.is_available():
        image_tensor = image_tensor.cuda()

    feature, (h_n, c_n) = encoder(image_tensor)
    inference_results = decoder.inference(feature.squeeze(0))

    sentences = []

    for i, result in enumerate(inference_results):
        words = []
        for word_id in result:
            word = vocab.idx2word[word_id.cpu().item()]
            words.append(word)
            if word == '<end>':
                break
                
        words.remove('<start>')
        try:
            words.remove('<end>')
        except Exception:
            pass
            
        sentences.append(' '.join(words).replace(' .', '.').capitalize())

    story = '\n'.join(sentences)
    
    return story

def generate_narration(story):
    tts = gTTS(story, lang='en', tld='co.uk')
    tmp_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.mp3'
    tts.save(tmp_file)
    audio, sr = librosa.load(tmp_file)
    os.remove(tmp_file)
    
    return (sr, audio)


def process(files):
    file_paths = [f.name for f in files]
    file_names = [os.path.basename(p).split('.')[0] for p in file_paths]
    
    file_paths, file_names = \
        zip(
            *sorted(zip(file_paths, file_names), 
                    key=lambda x: (int(x[1].split('_')[0])
                                   if x[1].split('_')[0].isdigit() else -1))
        )
    images = [Image.open(p).convert('RGB') for p in file_paths]
    concatenated_img = hconcat_resize([np.array(i) for i in images])
    
    story = generate_story(images)
    
    narration = generate_narration(story)
    
    return concatenated_img, story, narration


description='''
This application generate a story transcript from a sequence of image.
\n
\n
Please name the images in numerical order (e.g.  1.jpg, 2.png, 3.jpeg etc.), or 
else the sequence of images will be shuffled.
\n
It is recommended that the number of images is at most 5 and their sizes are as 
small as possible.
'''

iface = gr.Interface(fn=process, 
                     inputs=gr.inputs.File(file_count='multiple',
                                               type='file',
                                               keep_filename=True,
                                               label='Files upload'), 
                     outputs=[gr.outputs.Image('auto', label='Image sequence'),
                              gr.outputs.Textbox('auto', label='Generated story'),
                              gr.outputs.Audio(type='auto', label='Voice narration')],
                     layout='vertical',
                     title='MVP: Visual Storytelling',
                     description=description,
                     article='Taiwan Bootcamp 2021 - Cinnamon AI',
                     allow_flagging=False,
                     allow_screenshot=True,
                     )

if __name__ == '__main__':
    iface.launch(share=True)