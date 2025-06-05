// Toggles an LED on and off on each button press
// Alternatively, you could trigger the toggle on the falling edge
// But you cannot use an arbitrary change of state as it will cause two toggles in one press
// dt must be high enough to account for the bounce of the push button
// Try making an event onButtonPress and a create a callback for toggling the LED

int baudRate = 9600;
int ledState = 0;
int ledPin = 8;
int buttonPin = 12;
int buttonStateNew;
int buttonStateOld = 1; // Recall, this is a pull-up resistor which indicates off when the signal is 1 and on when the signal is 0 (pressed down)
int dt = 100;

void setup() {
  Serial.begin(baudRate);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  // Read the new button state
  buttonStateNew = digitalRead(buttonPin);

  // The rising edge of the button switch
  if (buttonStateOld == 0 && buttonStateNew == 1) {
    // If the led is off, turn it on
    // Else, the led is on, turn it off
    if (ledState == 0) {
      digitalWrite(ledPin, HIGH);
      ledState = 1;
    } else {
      digitalWrite(ledPin, LOW);
      ledState = 0;
    }
  }

  // Record the last button state
  buttonStateOld = buttonStateNew;
  delay(dt);

}
