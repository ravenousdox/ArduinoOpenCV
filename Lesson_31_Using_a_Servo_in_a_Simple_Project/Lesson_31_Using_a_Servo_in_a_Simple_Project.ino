// Lesson 31 Using a Servo in a Simple Project
// Actuates a servo with a pointer based on the light level read
// The pointer falls on a guage and indicates whether it is day or night

#include <Servo.h>

int baudRate = 9600;
int dt = 250;
int photoresistorPin = A4;  // An analog pin for reading analog values [0-1023]
int servoPin = 9;

// The current light value read, the light value as a voltage, and the angle to actuate the servo by
int lightLevel, lightVoltage, angle;
// The maximum and minimum natural light value
int maxLightLevel, minLightLevel;
// The maximum and minimum operating angles for the servo actuator
int maxServoAngle, minServoAngle;

Servo servoObject;

void setup() {
  Serial.begin(baudRate);
  pinMode(photoresistorPin, INPUT);
  pinMode(servoPin, OUTPUT);

  servoObject.attach(servoPin);
}

void loop() {
  // Reads the current light level as an analog value
  lightLevel = analogRead(photoresistorPin);
  
  // Converts the analog value as a voltage [0v, 5v]
  lightVoltage = lightLevel * 5./1023;
  
  // Calculates the angle to actuate the servo
  angle = (lightLevel - minLightLevel) * (maxServoAngle - minServoAngle) / (maxLightLevel - minLightLevel);
  // If operating servo angle range is [0, 180], light level range is [0, 1023]
  // If maximum light value read: (1023 - 0) * (180 - 0) / (1023 - 0) == 1023 * 180 / 1023 == 180
  // If minimum light value read: (0 - 0) * (180 - 0) / (1023 - 0) == 0 * 180 / 1023 == 0

  // Actuates the servo by the angle calculated
  servoObject.write(angle);

  // Prints out the relevant information 
  Serial.println("Light Level: ");
  Serial.print(lightLevel);
  Serial.print(", Light Voltage: ");
  Serial.print(lightVoltage);
  Serial.print("V, Angle: ");
  Serial.print(angle);

  delay(dt);
}
