import os
import pickle
import face_recognition as fr
import cv2
print(cv2.__version__)

encodings = []
names = []

images = r'demoImages'

for root, dirs, files in os.walk(images):
	for file in files:
		path = root + '\\' + file
		name = file[:-4]

		img = fr.load_image_file(path)
		encoding = fr.face_encodings(img)[0]

		encodings.append(encoding)
		names.append(name)

with open ('train.pkl', 'wb') as f:
	pickle.dump(names, f)
	pickle.dump(encodings, f)
