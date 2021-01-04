import pyrealsense2 as rs
import numpy as np
import cv2
import time

# Configure depth and color streams
pipeline = rs.pipeline()

config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
profile = pipeline.start(config)

# Getting the depth sensor's depth scale (see rs-align example for explanation)
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)

# We will be removing the background of objects more than
#  clipping_distance_in_meters meters away
clipping_distance_in_meters = 1 #1 meter
clipping_distance = clipping_distance_in_meters / depth_scale

# Create an align object
# rs.align allows us to perform alignment of depth frames to others frames
# The "align_to" is the stream type to which we plan to align depth frames.

align_to = rs.stream.color
align = rs.align(align_to)
imgforder_name = 'rgb/'
depforder_name = 'depths/'
imgfile_name = 'rgb'
depfile_name = 'depth'
file_form = '.png'

f_rgb = open('rgb.txt', 'w')
f_depth = open('depth.txt','w')
t_init = time.time()



#initialize
for i in range(30):
    t1 = pipeline.wait_for_frames()


print(" \'s\' key: start button")
print(" ctrl + c key: end   button")


i = 0
flag = 0

input_key = raw_input()

try:
	while True:
		i += 1
		# Wait for a coherent pair of frames: depth and color
		frames = pipeline.wait_for_frames()
		aligned_frames = align.process(frames)

		color_frame = aligned_frames.get_color_frame()
		depth_frame = aligned_frames.get_depth_frame()
        
		#if not depth_frame or not color_frame:
		#    continue

		# Convert images to numpy arrays
		color_image = np.asanyarray(color_frame.get_data())
		depth_image = np.asanyarray(depth_frame.get_data())

		# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
		depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

		t = time.time()
		#depth_image = depth_image*1000.0*depth_scale 

		if flag:
			cv2.imwrite(imgforder_name + imgfile_name + str(i).zfill(5) + file_form, color_image)
			cv2.imwrite(depforder_name + depfile_name + str(i).zfill(5) + file_form, depth_image)        
			f_rgb.write(str(t-t_init).zfill(16) + ' ' + imgforder_name + imgfile_name + str(i).zfill(5) + file_form  + '\n')
			f_depth.write(str(t-t_init).zfill(16) + ' ' + depforder_name + depfile_name + str(i).zfill(5) + file_form  + '\n')
			print((t-t_init))
		
		cv2.namedWindow('RealSense_RGB', cv2.WINDOW_AUTOSIZE)
		cv2.imshow('RealSense_RGB', color_image)
		cv2.namedWindow('RealSense_Depth', cv2.WINDOW_AUTOSIZE)
		cv2.imshow('RealSense_Depth', depth_colormap)

		key = cv2.waitKey(1)
		#print(i)

		if input_key == 's':
			t_init = time.time()
			flag = 1
			#i = 0
			#print('hi')
						
		elif key == 27:
			break 

finally:
    f_rgb.close()
    f_depth.close()
    # Stop streaming
    pipeline.stop()
