// Lesson 33 Understanding How to Control Servos with a Joystick
// Uses a joystick to aim two servos
// You could hook up a laser or arm, and trigger them using the joystick button
// Currently, it just sounds a buzzer

#include <Servo.h>

int baudRate = 9600;
int dt = 250;

// Analog pins for the x and y potentiometers in the joystick
// Pin for the push button in the joystick
int xJoystickPin = A0;
int yJoystickPin = A1;
int joystickButtonPin = 2;

int xServoPin = 9;
int yServoPin = 10;

int buzzerPin = 7;

// Holds the x and y analog values for the joystick and whether the state of the joystick button
int xJoystickVal, yJoystickVal, joystickButtonState;
// Holds the angle to revolve the servo actuator by
int xServoAngle, yServoAngle;

// The servo for controlling the x-direction and y-direction
Servo xServo, yServo;

void setup() {
  Serial.begin(baudRate);

  pinMode(xJoystickPin, INPUT);
  pinMode(yJoystickPin, INPUT);
  pinMode(joystickButtonPin, INPUT);

  pinMode(xServoPin, OUTPUT);
  pinMode(yServoPin, OUTPUT);

  pinMode(buzzerPin, OUTPUT);

  // Attaches the servos to their respective servo objects
  xServo.attach(xServoPin);
  yServo.attach(yServoPin);

  // Creates an internal pull-up resistor
  digitalWrite(joystickButtonPin, HIGH);
}

void loop() {
  xJoystickVal = analogRead(xJoystickPin);
  yJoystickVal = analogRead(yJoystickPin);
  joystickButtonState = digitalRead(joystickButtonPin);

  // Converts the analog value read from the joystick to a float angle in [0, 180]
  // If the servo's range is different --> xJoystickVal * (maxServoAngle - minServoAngle)/1023. + minServoAngle (I believe?)
  
  xServoAngle = xJoystickVal * (180./1023);
  yServoAngle = yJoystickVal * (180./1023);

  xServo.write(xServoAngle);
  yServo.write(yServoAngle);

  // If joystick button is pressed (0), sound the buzzer
  // If joystick button is not pressed (1), silence the buzzer
  joystickButtonState ? digitalWrite(buzzerPin, LOW) : digitalWrite(buzzerPin, HIGH);

  Serial.print("xJoystickVal: ");
  Serial.print(xJoystickVal);
  Serial.print(", yJoystickVal: ");
  Serial.print(yJoystickVal);
  Serial.print(", joystickButtonState: ");
  Serial.println(joystickButtonState);

  Serial.print("xServoAngle: ");
  Serial.print(xServoAngle);
  Serial.print(", yServoAngle: ");
  Serial.println(yServoAngle);

  delay(dt);
}
