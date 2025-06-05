// Lesson 39 Using a Joystick to Control DC Motor
// Uses the vertical potentiometer on the joystick to control the speed and direction of the DC motor

int baudRate;

int speedPin = 5;
int forwardPin = 4;
int backwardPin = 3;

int joystickPin = A1;

int joystickVal, motorSpeed;

void setup() {
  Serial.begin(baudRate);
  
  pinMode(speedPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);
  pinMode(joystickPin, INPUT);
}

void loop() {
  joystickVal = analogRead(joystickPin);

  Serial.print("Joystick Value: ");
  Serial.println(joystickVal);

  // If joystick is pointed north, increase speed linearly and direction is counter-clockwise
  // Convert joystick value to (512, 1023] -> (0, 255]
  if (joystickVal > 512) {
    motorSpeed = 255./512 * joystickVal - 255;
    digitalWrite(forwardPin, HIGH);
    digitalWrite(backwardPin, LOW);
    analogWrite(speedPin, motorSpeed);
  }

  // If joystick is not moved in any direction, stop motor
  if (joystickVal == 512)
    analogWrite(speedPin, LOW);

  // If joystick is pointed south, increase speed linearly and direction is clockwise
  // Convert joystick value to (512, 0] -> (0, 255]
  if (joystickVal < 512) {
    motorSpeed = -255./512 * joystickVal + 255;
    digitalWrite(forwardPin, LOW);
    digitalWrite(backwardPin, HIGH);
    analogWrite(speedPin, motorSpeed);
  }
  
}
