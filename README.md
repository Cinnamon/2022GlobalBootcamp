# 2022GlobalBootcamp
Lecture material for Global Summer Bootcamp

## Installation

Python  or Anaconda, if you choose to use `pip` to install package, we
recommend using `virtualenv` to manage your environment.

Below are the steps to setup the required packages for bootcamp's excercises.
### Install by pip

```
pip install -r requirements.txt
```

### Install by conda

```
conda create --name <env_name> --file requirements.txt python=3.6
conda activate <env_name>
```

### Install PyTorch

PyTorch requires different command based on your environment. In this course,
we will use PyTorch 1.12.0 (which is latest at the moment). You choose the
command to install by accessing the following link:

[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

### Install Docker desktop

Docker desktop already provide the docker engine and docker-compose, you may download all platform's docker-desktop in [offcial website](https://www.docker.com/products/docker-desktop/)

After installation, type below command into your terminal to see if the installation is successfully done.
        
    docker --version
    docker-compose --version
    '''
    You should see output like this:
    
    Docker version 18.09.2, build 6247962
    docker-compose version 1.23.2, build 1110ad01
    '''


### Syllabus

| Date | Subject |
|--- | --- |
| Jun 30 | <ul>**Bootcamp Opening Day**</ul><li>TW&VN Mentor / Lecturer introduction</li><li>Futurist of Cinnamon - Hajime’s sharing</li><li>Syllabus Introduction</li><li>Ice-break</li> |
Jul 5 | <ul>**Lean startup**</ul><li>Lean Startup(Paul)</li>|
Jul 7 | <ul>**MVP project**</ul><li>Life Cycle of ML project (Mandy)</li>|
Jul 12 | <ul>**Agile Software development**</ul><li>SCRUM (Hato)</li>|
Jul 14 | <ul>**Agile Software development**</ul><li>+Git Workflow (Blake)</li> |
Jul 19 | <ul>**Agile Software development**</ul><li>Clean code (Vincent)</li><li>SOLID (Vincent)</li>|
Jul 21 | <ul>**Agile Software development**</ul><li>Docker Introduction (Jayce)</li>|
Jul 26 | <ul>**Data Loader (Dini)**</ul><li>Dataset and data loader in PyTorch</li><li>Efficient Training</li>|
Jul 28 | <ul>**Deep Learning Class (Hy)**</ul><li>Loss Function</li><li>CrossEntropy</li><li>MSE</li><li>TripletLoss</li><li>HubertLoss</li>|
Aug 2 | <ul>**NLP Technical Class [1] (Dini)**</ul><li>Missions & Metrics and Preprocessing</li>|
Aug 4 | <ul>**NLP Technical Class [2] (Matt)**</ul><li>Language modelling</li><li>Language models: n-gram, RNN, CNN, Transformer</li>|
Aug 9 | <ul>**NLP Technical Class [3]  (Matt)**</ul><li>Pre-trained models: ELMo, GPT, BERT</li>|
Aug 11 | <ul>**NLP Technical Class [4] (Hubert)**</ul><li>information extraction </li><li>explain real-business case and material </li>|
Aug 16 | <ul>**CV Technical Class [3] (Tyler)**</ul><li>Training Tricks</li><li>Stochastic Depth</li><li>Warm up</li><li>Label Smoothing</li><li>No Bias Weight Decay</li><li>Teacher-Student Knowledge Distillation</li><li>Mixup</li><li>Group Normalization</li><li>Weight Standardization</li>|
Aug 18 | <ul>**CV Technical Class [1]  (Jeff)**</ul><li>ClassicCNN</li>|
Aug 23 | <ul>**CV Technical Class [2] (Vincent)**</ul><li>VisionTransformers</li>|
Aug 25 | **Presentation (Paul)**|
Aug 30 | **Rehearsal** |
Sep (TBD) | **Demo Day** |

