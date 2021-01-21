import cv2
import time

bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

cap = cv2.VideoCapture('traffic.flv')
prev_frame_time = 0
new_frame_time = 0
success, frame = cap.read()
time_treshold = 1
counter = 0
while success:
	fg_mask = bg_subtractor.apply(frame)
	_, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
	cv2.erode(thresh, erode_kernel, thresh, iterations=2)
	cv2.dilate(thresh, dilate_kernel, thresh, iterations=5)
	contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		if cv2.contourArea(c) > 5000:
			x, y, w, h = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
	#~ new_frame_time = time.time() 
	#~ fps = (new_frame_time-prev_frame_time) 
	#~ fps = int(fps) 
	#~ fps = str(fps)
	#~ fps = (fps + " fps") 
	#~ prev_frame_time = new_frame_time
	#~ fps = str(fps)
	#~ print(fps)
	counter = counter + 1
	font = cv2.FONT_HERSHEY_SIMPLEX 
	new_frame_time = time.time() 
	if new_frame_time - prev_frame_time >= time_treshold:
		fps = counter/(new_frame_time-prev_frame_time) 
		fps = int(fps) 
		fps = str(fps)
		fps = (fps + " fps") 
		prev_frame_time = new_frame_time
		counter = 0
	cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
	cv2.imshow('thresh',thresh)
	cv2.imshow('mog', fg_mask)
	cv2.imshow('video', frame) 
	k = cv2.waitKey(1)
	if (k == ord('q')):
		break
	success, frame = cap.read()



