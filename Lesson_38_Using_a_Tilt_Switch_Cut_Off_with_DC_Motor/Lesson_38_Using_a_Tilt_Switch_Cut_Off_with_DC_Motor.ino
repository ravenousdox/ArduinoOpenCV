// Lesson 38 Using a Tilt Switch Cut Off With a DC Motor
// This program rotates a tilt switch with a DC motor
// When the tilt switch triggers, the speed to the DC motor is cut
// Pin 3 on Motor Controller is VCC for DC Motor
// Pin 4 on Motor Controller is GND
// Pin 6 on Motor Controller is GND for DC Motor
// Pin 8 on Motor Controller is VCC

int baudRate = 9600;

int speedPin = 5;         // Connects to pin 1 on motor controller
int forwardPin = 4;       // Connects to pin 2 on motor controller
int backwardPin = 3;      // Connects to pin 7 on motor controller
int tiltPin = 2;
int motorSpeed = 100;     // Minimum motor speed for movement from rest is 100 for my DC motor
int tiltState;

void setup() {
  Serial.begin(baudRate);
  
  pinMode(speedPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);
}

void loop() {
  tiltState = digitalRead(tiltPin);
  
  Serial.print("Tilt State: ");
  Serial.println(tiltState);

  if (!tiltState)
    analogWrite(speedPin, motorSpeed);
    // analogWrite(speedPin, HIGH);
  else
    analogWrite(speedPin, 0);
    // analogWrite(speedPin, LOW);
}
