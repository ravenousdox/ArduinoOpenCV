// Turns an LED on and off every 2 seconds

int ledPin = 13;
int oneSecond = 1000;   // one second in ms

void setup() {
  // Outputting a signal to the LED
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turning the LED on (writing HIGH or 1)
  digitalWrite(ledPin, HIGH);
  // Waiting one second
  delay(oneSecond);
  // Turning the LED off (writing LOW or 0)
  digitalWrite(ledPin, LOW);
  // Waiting one second
  delay(oneSecond);
}
