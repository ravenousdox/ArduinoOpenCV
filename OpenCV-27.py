import pickle
import time
import face_recognition as fr
import cv2
print(cv2.__version__)

font = cv2.FONT_HERSHEY_SIMPLEX
width = 1280
height = 720
fps = 10
initTime = time.time()

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

with open('train.pkl', 'rb') as f:
	names = pickle.load(f)
	knownEncodings = pickle.load(f)

while True:
    _, frame = cam.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faceLocations = fr.face_locations(frameRGB)
    unknownEncodings = fr.face_encodings(frameRGB, faceLocations)

    for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
        top, right, bottom, left = faceLocation
        #print(faceLocation)

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 3)

        matches = fr.compare_faces(knownEncodings, unknownEncoding)
        #print(matches)

        name = 'Unknown Person'

        if True in matches:
            matchIndex = matches.index(True)
            name = names[matchIndex]
            #print(names[matchIndex])

        cv2.putText(frame, name, (left, top - 7), font, 0.75, (0, 0, 255), 2)
        
    loopTime = time.time() - initTime
    initTime = time.time()
    fpsNew = 1/loopTime
    fps = int(0.9 * fps + 0.1 * fpsNew)
    cv2.putText(frame, str(fps) + ' fps', (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()