// Lesson 40 Controlling DC Motor Speed and Direction using Pushbuttons
// This program has two buttons: One for increasing motor speed and one for decreasing motor speed
// The range of speed is [-255, -95) U (95, 255] with step values of +-10
// If the speed is negative, the motor moves in a clockwise direction
// If the speed is positive, the motor moves in a counter-clockwise direction
// The motor stops running at speed values of |+-100| and below

int baudRate = 9600;
int tenthSecond = 100;

int speedPin = 5;
int forwardPin = 4;
int backwardPin = 3;
int upperButtonPin = 8;
int lowerButtonPin = 9;
int upperButtonState, lowerButtonState;
int motorSpeed = 0;

void setup() {
  Serial.begin(baudRate);
  
  pinMode(speedPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);
  pinMode(upperButtonPin, INPUT);
  pinMode(lowerButtonPin, INPUT);
  
  // Internal Pull-Up Resistors
  digitalWrite(upperButtonPin, HIGH);
  digitalWrite(lowerButtonPin, HIGH);
}

void loop() {
  upperButtonState = digitalRead(upperButtonPin);
  lowerButtonState = digitalRead(lowerButtonPin);

  Serial.print("Upper Button: ");
  Serial.print(upperButtonState);
  Serial.print(", Lower Button: ");
  Serial.println(lowerButtonState);

  Serial.print("Motor Speed: ");
  Serial.println(motorSpeed);

  if (!upperButtonState) {
    motorSpeed += 10;
    delay(tenthSecond);
  }

  if (!lowerButtonState) {
    motorSpeed -= 10;
    delay(tenthSecond);
  }

  // Ensure doesn't go over maximum speed
  if (motorSpeed > 255)
    motorSpeed = 255;

  // If speed falls between minimum operating speed, turn off motor
  // Additionally, since motor speed is changed by increments of 10, ensure that this occurs under either of the conditions
  if (motorSpeed == 90 || motorSpeed == 95)
    motorSpeed = 0;

  if (motorSpeed == 10)
    motorSpeed = 100;

  if (motorSpeed == -10)
    motorSpeed = -100;

  if (motorSpeed == -90 || motorSpeed == -95)
    motorSpeed = 0;

  if (motorSpeed < -255)
    motorSpeed = -255;

  // Turn the motor off
  if (motorSpeed == 0)
    analogWrite(speedPin, LOW);

  // Counter-Clockwise motion
  if (motorSpeed > 0) {
    digitalWrite(forwardPin, HIGH);
    digitalWrite(backwardPin, LOW);
    analogWrite(speedPin, abs(motorSpeed);
  }

  // Clockwise motion
  if (motorSpeed < 0) {
    digitalWrite(forwardPin, LOW);
    digitalWrite(backwardPin, HIGH);
    analogWrite(speedPin, motorSpeed);
  }
}
