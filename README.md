# Make-ORB-SLAM2-RGBD-dataset

This repository helps you make Custom Dataset (RGB-D) used in [ORB_SLAM2](https://github.com/raulmur/ORB_SLAM2).  

When you excute ORB_SLAM2 RGB-D mode with your own dataset, you need to create  
- `rgb.txt` : the timestamps and RGB images list  
- `depth.txt` : the timestamps and depth images list  
- `association.txt` : the list of matching timestamp, rgb filename, timestamp, and depth filename.  
- `rgb/` : the folder of RGB image sequence
```
- rgb /  
    |---- rgb00002.png
    |---- rgb00003.png
    |---- rgb00004.png
    |---- rgb00005.png ..
```
- `depths/` : the folder of depth image sequence
```
- depths /  
    |---- depth00002.png
    |---- depth00003.png
    |---- depth00004.png
    |---- depth00005.png ..
```  

### You can make these things with Real Sense Camera! :blush:  

I tested this repository with **Real Sense D435 & L515!**  

## 1. Prerequisites  
- pyrealsense2  
- numpy  
- opencv-python  
- python  

## 2. Make RGB and depth sequence  
With `rs-get-Sequence.py` you could get RGB and depth sequence.  

First you would make empty folders which name `rgb/` and `depths/`.  
After you connect your real sense camera, just run the `python rs-get-Sequence.py` in terminal.  

When you run this code, press 's' button and 'enter' to start.  
You could visualize `RGB image` and `Depth colorized image`.  
And save images and `rgb.txt` and `depth.txt`!  




