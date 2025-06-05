f1 = open('patientData.txt', 'r')
Data = f1.readlines()
for patient in Data:
	patientData = patient.split(', ')
	print('Name: ' + patientData[0])
	print('Number: ' + patientData[1])
	print('Facility: ' + patientData[2])
f1.close()
