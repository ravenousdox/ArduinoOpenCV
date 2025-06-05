// Lesson 32 Understanding and Using Joysticks
// The joystick is basically two potetiometers
// One reading an up/down direction, and the other reading a left/right direction

int baudRate = 9600;
int dt = 250;

// Analog pins for reading analog potentiometer values
int xJoystickPin = A0;
int yJoystickPin = A1;
int buttonJoystickPin = 2;

int xJoystickVal, yJoystickVal, joystickButtonState;

void setup() {
  Serial.begin(baudRate);

  pinMode(xJoystickPin, INPUT);
  pinMode(yJoystickPin, INPUT);
  pinMode(buttonJoystickPin, INPUT);

  // Internal pull-up resistor
  digitalWrite(buttonJoystickPin, HIGH);
}

void loop() {
  xJoystickVal = analogRead(xJoystickPin);
  yJoystickVal = analogRead(yJoystickPin);
  joystickButtonState = digitalRead(buttonJoystickPin);

  Serial.print("xJoystickVal: ");
  Serial.print(xJoystickVal);
  Serial.print(", yJoystickVal: ");
  Serial.print(yJoystickVal);
  Serial.print(", joystickButtonState: ");
  Serial.println(joystickButtonState);
  
  delay(dt);
}
