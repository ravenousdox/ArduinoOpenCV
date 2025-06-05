// Lesson 36 Understanding Tilt Switches
// This program signals a green LED to turn on when untilted and a red LED to turn on when tilted

int baudRate = 9600;

int tiltPin = 2;
int redPin = 7;
int greenPin = 6;

int tiltState;

void setup() {
  Serial.begin(9600);
  
  pinMode(tiltPin, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);

  // Internal pull-up resistor
  digitalWrite(tiltPin, HIGH);
}

void loop() {
  tiltState = digitalRead(tiltPin);

  Serial.print("Tilt State: ");
  Serial.print(tiltState);

  if (!tiltState) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(redPin, LOW);
  } else {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, HIGH);
  }
}
