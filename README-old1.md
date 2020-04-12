# Documentation

**Project** - Sacchi disc detection on provided video. Train a model. Detect 
Sachhi disc from trained model on a given video and identify frame where
disc disappears.

**Input Video** - Input video are upload at this link.

<https://drive.google.com/drive/folders/1XX2eI-6uBgdlGP62csvoW-kyXc4Twdgv>

## Installation (In Progress)

* Cloudmesh
* LabelImg
* tensorflow
* Keras

```
    pip install cloudmesh-installer
    cloudmesh-installer git clone cms
    cloudmesh-installer install cms
    # git clone git@github.com:cloudmesh/cloudmesh-secchi.git
    git clone https://github.com/cloudmesh/cloudmesh-secchi.git
    cd cloudmesh-secchi
    pip install -e . 
```

## Objective:

To detect secchi disk in provided video using object detection algorithms and 
integrate this module into cloudmesh. Final objective is to locate the frame 
where the Sacchi disk disappears. 

Usage:

```
                secchi upload [VIDEO] [--training]
                secchi list [VIDEO]
                sechhi delete VIDEOS
                secchi server start
                secchi server stop
                secchi server status
                secchi labelImg install
                secchi labelImg run
                secchi captureImage

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file
              
```              

## Outline

* Upload a video or multiple video for training
* Create image frame from video using labelImg for training -- one time activity
* Train video/s to identify Secchi disk object
* Generate weights
* Upload a video to predict Predict(identify Secchi disk) by using generated weights.
* Identify frame where Secchi disk disappears.