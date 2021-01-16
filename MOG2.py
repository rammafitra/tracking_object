import cv2

bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

cap = cv2.VideoCapture('hallway.mpg')
success, frame = cap.read()
while success:
	fg_mask = bg_subtractor.apply(frame)
	_, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
	cv2.erode(thresh, erode_kernel, thresh, iterations=2)
	cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)
	contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		if cv2.contourArea(c) > 1000:
			x, y, w, h = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
	cv2.imshow('thresh',thresh)
	cv2.imshow('mog', fg_mask)
	cv2.imshow('video', frame)
	k = cv2.waitKey(30)
	if (k == ord('q')):
		break
	success, frame = cap.read()


""" NOTE:: backgroundSubtractorMOG2 : bgsubtrcator yang menerapkan Gaussian Mixture Model
		   thresh : batas bawah yang digunakan adalah 244 (piksel dengan intensitas dibawah 244 maka akan menjadi black dan jika diatas 244 maka aka diubah menajdi putih)
		   tipe threshold yang digunakan adalah tipe cv2.THRESH_BINARY
		   pada cv2.findContours ada tiga parameter inputan (inputan, contours, hirarchy)
		   dimana cv2.RETR_EXTERNAL hanya mengambil kontour terluar dari suatu object, cv2.CHAIN_APPROX_SIMPLE 
		   """
