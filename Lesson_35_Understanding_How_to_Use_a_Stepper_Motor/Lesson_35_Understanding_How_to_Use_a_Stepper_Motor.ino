// Lesson 35 Understanding How to Use a Stepper Motor
// Stepper motors are motors with precise control, large torque at low RPM, and unlimited range of rotation
// Commonly used in projects requiring high precision and high torque, such as CNC, 3D Printers, and Laser Engravers
// For this stepper motor (28BYJ-48 ROHS), 2048 steps make a single revolution which is ~1/5 degrees per step (360/2048)
// This driver takes between 5V-12V, I am using 5V
// Power supply, driver, stepper motor

// This program instructs a stepper motor to do one forwards rotation and one backwards rotation

// Stepper motor library
#include <Stepper.h>

int stepsPerRevolution = 2048;
int motorSpeed = 10;            // Can not be set TOO high
int halfSecond = 500;

// Different drivers have different pin sequences
// For this stepper's driver, these are the pin sequences that are used (one for each coil in the stepper motor)
Stepper stepperObject(stepsPerRevolution, 8, 10, 9, 11);  // [IN1, IN2, IN3, IN4] -> [8, 9, 10, 11]

void setup() {
  Serial.begin(baudRate);

  stepperObject.setSpeed(motorSpeed);
}

void loop() {
  stepperObject.step(stepsPerRevolution);
  delay(halfSecond);
  stepperObject.step(-stepsPerRevolution);
  delay(halfSecond);
}
