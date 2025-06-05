# Moves a window on the screen based on the location of an OoI


import numpy as np
import cv2
print(cv2.__version__)

hueLow = 10
hueHigh = 20
hueLow2 = 10
hueHigh2 = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250
width = 640
height = 360
xPos = 0
yPos = 0

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

def onTrack7(val):
	global hueLow2
	hueLow2 = val
	print('Hue Low 2:', hueLow2)

def onTrack8(val):
	global hueHigh2
	hueHigh2 = val
	print('Hue High 2:', hueHigh2)

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Trackbar Window')
cv2.moveWindow('Trackbar Window', width, 0)

cv2.createTrackbar('Hue Low', 'Trackbar Window', 80, 179, onTrack1)
cv2.createTrackbar('Hue High', 'Trackbar Window', 100, 179, onTrack2)
cv2.createTrackbar('Hue Low 2', 'Trackbar Window', 10, 179, onTrack7)
cv2.createTrackbar('Hue High 2', 'Trackbar Window', 20, 179, onTrack8)
cv2.createTrackbar('Sat Low', 'Trackbar Window', 120, 255, onTrack3)
cv2.createTrackbar('Sat High', 'Trackbar Window', 255, 255, onTrack4)
cv2.createTrackbar('Val Low', 'Trackbar Window', 80, 255, onTrack5)
cv2.createTrackbar('Val High', 'Trackbar Window', 255, 255, onTrack6)

cv2.namedWindow('Camera')

while True:
	ignore, frame = cam.read()

	hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lowHSV = np.array([hueLow, satLow, valLow])
	highHSV = np.array([hueHigh, satHigh, valHigh])

	lowHSV2 = np.array([hueLow2, satLow, valLow])
	highHSV2 = np.array([hueHigh2, satHigh, valHigh])

	trackMask = cv2.inRange(hsvFrame, lowHSV, highHSV) 
	smallMask = cv2.resize(trackMask, (int(width/2), int(height/2)))

	trackMask2 = cv2.inRange(hsvFrame, lowHSV2, highHSV2) 
	smallMask2 = cv2.resize(trackMask2, (int(width/2), int(height/2)))

	compMask = trackMask | trackMask2
	contours, _ = cv2.findContours(compMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		area = cv2.contourArea(contour)
		if area >= 200:	
			x, y, w, h = cv2.boundingRect(contour)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
			xPos = int(x * (-1920/width) + 1920)
			yPos = int(y/height * 1080)

	trackROI = cv2.bitwise_and(frame, frame, mask = compMask) 
	smallROI = cv2.resize(trackROI, (int(width/2), int(height/2)))

	cv2.imshow('Small Region of Interest', smallROI)
	cv2.moveWindow('Small Region of Interest', int(width/2), height)

	cv2.imshow('Small Bitmap Mask', smallMask)
	cv2.moveWindow('Small Bitmap Mask', 0, height)

	cv2.imshow('Small Bitmap Mask 2', smallMask2)
	cv2.moveWindow('Small Bitmap Mask 2', 0, height + int(height/2) + 30)

	cv2.imshow('Camera', frame)
	cv2.moveWindow('Camera', xPos, yPos)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cam.release()