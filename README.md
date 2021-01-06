# Make-ORB-SLAM2-RGBD-dataset

This repository helps you make Custom Dataset (RGB-D) used in [ORB_SLAM2](https://github.com/raulmur/ORB_SLAM2).  

When you excute [ORB_SLAM2 RGB-D mode](https://github.com/raulmur/ORB_SLAM2#6-rgb-d-example) with your own dataset, you need to create  
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

## 3. Make a little modification about `rgb.txt` and `depth.txt`
When you get `rgb.txt` and `depth.txt`, It looks like this.  
For example `rgb.txt`,  
```
0.00585412979126 rgb/rgb00002.png
0.00706601142883 rgb/rgb00003.png
00.0154299736023 rgb/rgb00004.png
00.0148220062256 rgb/rgb00005.png
00.0163168907166 rgb/rgb00006.png
00.0162618160248 rgb/rgb00007.png
00.0166661739349 rgb/rgb00008.png
00.0166158676147 rgb/rgb00009.png
00.0157341957092 rgb/rgb00010.png
00.0166420936584 rgb/rgb00011.png
00.0167319774628 rgb/rgb00012.png ...
```

**You should fix this txt file to follow ORB_SLAM2 `rgb.txt` rules!**  

Just add these 3 lines to fit the format.  
```
# rgb maps
# file: 'example of rgb sequence'
# timestamp filename
```

You could get this result.

```
# rgb maps
# file: 'example of rgb sequence'
# timestamp filename
0.00585412979126 rgb/rgb00002.png
0.00706601142883 rgb/rgb00003.png
00.0154299736023 rgb/rgb00004.png
00.0148220062256 rgb/rgb00005.png
00.0163168907166 rgb/rgb00006.png
00.0162618160248 rgb/rgb00007.png
00.0166661739349 rgb/rgb00008.png
00.0166158676147 rgb/rgb00009.png
00.0157341957092 rgb/rgb00010.png
00.0166420936584 rgb/rgb00011.png
00.0167319774628 rgb/rgb00012.png ...
```

## 4. Make `associations.txt`   

You could make `associations.txt` with `associate.py`.  
When you run `associate.py`, you need to provide 3 argments.  
- rgb_path : Path of rgb.txt  
- depth_path : Path of depth.txt  
- output : Output name of txt file  

You run the code like this.  
- `python associate.py --rgb_path [rgb path] --depth_path [depth path] --output [Name of txt file]`.  
- (For example) `python associate.py --rgb_path rgb.txt --depth_path depth.txt --output associations.txt`.  

### It's Done! Just excute ORB_SLAM2 RGB-D Mode :satisfied:
