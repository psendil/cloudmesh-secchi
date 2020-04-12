# To run model

## Prerequisite

Python 3.6
Tensorflow 1.14
Pillow
lxml
matplotlib
opencv
cython

## Create virtual environment with python 3.6

```
python -m venv ENVTF1.14
``` 

## Activate environment

```
ENVTF1.14\Scripts\activate

```
## Installation

```
pip install --ignore-installed --upgrade tensorflow==1.14
pip install pillow, lxml, matplotlib, opencv-python, cython

```

## command line execution

### Upload video file to src folder through cms command

```
cms secchi upload '~/Desktop/file.mp4' --predict
```

### Run predict through cms command

```
cms secchi run --predict
```

### Get the graph output

```

cms secchi show graph

```

### Predict Screen and Graph

Example of prediction video and graph is shown:

![Output Graph](image/mygraph.png) 

![Predictor Output Image](image/Predictor_Image.png)