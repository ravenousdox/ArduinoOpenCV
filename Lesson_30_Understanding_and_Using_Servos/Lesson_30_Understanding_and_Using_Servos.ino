// Lesson 30 Understanding and Using Servos
// Asks the operator to input an angle into the Serial Monitor
// Rotates the servo actuator by the angle they enter
// Careful not to overdrive the servo motor by entering too high of an angle
// Cheap servos often do not have full range
// Ensure the arduino can output a current high enough to drive the servo, if not, use an external power supply

// The Servo library for handling servo motors
#include <Servo.h>

int baudRate = 9600;
int servoPin = 9;
int servoPosition = 0;

// Initializes a servo object for interfacing with the servo motor
Servo servoObject;

void setup() {
  Serial.begin(baudRate);

  // Attaches the servo to the servo object
  servoObject.attach(servoPin);
}

void loop() {
  Serial.println("Enter the angle [0~180] to actuate the servo: ");
  // While the serial buffer is empty, wait
  while (!Serial.available()) {}

  // Parse the data in the buffer as an integer
  // Signal the servo actuator to rotate by that amount
  servoPosition = Serial.parseInt();
  servoObject.write(servoPosition);
}
