import names
import random

names.get_full_name()
validNums = ['09', '08', '06']
validFacility = ['Overton', 'Kemp']

f1 = open('patientData.txt', 'a')

for patient in range(50):
	name = names.get_full_name()
	num = validNums[random.randint(0, 2)]
	facility = validFacility[random.randint(0, 1)]
	patientData = name + ', ' + num + ', ' + facility + '\n'
	f1.write(patientData)
f1.close()
