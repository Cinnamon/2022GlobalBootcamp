import cv2
import torch
from PIL import Image

def vconcat_resize(img_list, interpolation 
                   = cv2.INTER_CUBIC):
  # take minimum width
    w_min = min(img.shape[1] 
                for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img,
                      (w_min, int(img.shape[0] * w_min / img.shape[1])),
                                 interpolation = interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)


def hconcat_resize(img_list, interpolation 
                   = cv2.INTER_CUBIC):
  # take minimum height
    h_min = min(img.shape[0] 
                for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img,
                      (int(img.shape[1] * h_min / img.shape[0]), h_min),
                                 interpolation = interpolation)
                      for img in img_list]
    # return final image
    return cv2.hconcat(im_list_resize)


def transform_image(image, transform=None):
    image = image.resize([224, 224], Image.LANCZOS)
  
    if transform is not None:
        image = transform(image).unsqueeze(0)
  
    return image