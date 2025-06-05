import numpy as np
import cv2
print(cv2.__version__)

hueLow = 90
hueHigh = 100
satLow = 20
satHigh = 200
valLow = 20
valHigh = 200
width = 960
height = 540

def onTrack1(val):
    global hueLow
    hueLow = val
    print('Hue Low:', hueLow)

def onTrack2(val):
	global hueHigh
	hueHigh = val
	print('Hue High:', hueHigh)

def onTrack3(val):
	global satLow
	satLow = val
	print('Sat Low:', satLow)

def onTrack4(val):
	global satHigh
	satHigh = val
	print('Sat High:', satHigh)

def onTrack5(val):
	global valLow
	valLow = val
	print('Val Low:', valLow)

def onTrack6(val):
	global valHigh
	valHigh = val
	print('Val High:', valHigh)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Trackbar Window')
cv2.moveWindow('Trackbar Window', width, 0)
cv2.resizeWindow('Trackbar Window', 400, 500)

cv2.createTrackbar('Hue Low', 'Trackbar Window', 15, 180, onTrack1)
cv2.createTrackbar('Hue High', 'Trackbar Window', 30, 180, onTrack2)
cv2.createTrackbar('Sat Low', 'Trackbar Window', 10, 255, onTrack3)
cv2.createTrackbar('Sat High', 'Trackbar Window', 255, 255, onTrack4)
cv2.createTrackbar('Val Low', 'Trackbar Window', 10, 255, onTrack5)
cv2.createTrackbar('Val High', 'Trackbar Window', 255, 255, onTrack6)

while True:
	ignore, frame = cam.read()

	hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lowHSV = np.array([hueLow, satLow, valLow])
	highHSV = np.array([hueHigh, satHigh, valHigh])

	trackMask = cv2.inRange(hsvFrame, lowHSV, highHSV) 
	trackMask = cv2.bitwise_not(trackMask) 
	smallMask = cv2.resize(trackMask, (int(width/2), int(height/2)))

	myROI = cv2.bitwise_and(frame, frame, mask = trackMask) 
	smallROI = cv2.resize(myROI, (int(width/2), int(height/2)))

	contours, junk = cv2.findContours(trackMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		area = cv2.contourArea(contour)
		if area >= 200:
			x, y, w, h = cv2.boundingRect(contour)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,255), 3)

	cv2.imshow('Small Region of Interest', smallROI)
	cv2.moveWindow('Small Region of Interest', int(width/2), height)

	cv2.imshow('Small Bitmap Mask', smallMask)
	cv2.moveWindow('Small Bitmap Mask', 0, height)

	cv2.imshow('Camera', frame)
	cv2.moveWindow('Camera', 0, 0)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cam.release()