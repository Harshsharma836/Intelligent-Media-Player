import numpy as np 			# For efficient utilization of array
import cv2  				# Computer vision library
import os 				# Here this package is used writing CLI commands
import vlc_ctrl 			# package used for controlling vlc media player

# For caturing the frame from the camera 
cap = cv2.VideoCapture(0) 

# The path to the video to be played [ "Change it according to your needs" ]
os.system("vlc-ctrl play -p /home/akshath/Majmu_MediaPlayer/Video") 

# Frontal face classifier is imported here
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# Flag is used to pause and play the video [ if flag is 1 then the video plays else it doesn't ]
Pauseflag = 0 

try:
	while True:
		ret , img = cap.read() # For caturing the frame 
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# Gets the x and y coordinates of the face as well the width and height of the face if detected 
		for (x, y, w, h) in faces:
			print ("Face is facing front")
			os.system("vlc-ctrl play")
			Pauseflag = 1 # Face is detected hence play the video continuesly

		if Pauseflag == 0: # Face is not facing front hence pause the video
			print ("Face is not facing front")
			os.system("vlc-ctrl pause")
		Pauseflag = 0 

except KeyboardInterrupt:
	print ("Closing the application!!! [Interrupted]") 

cap.release() 



