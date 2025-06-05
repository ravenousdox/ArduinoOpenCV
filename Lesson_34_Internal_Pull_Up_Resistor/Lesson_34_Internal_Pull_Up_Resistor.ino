// Lesson 34 Internal Pull-Up Resistor
// When you write to an input pin "HIGH", it bridges the input to 5V
// This signal travels to an internal GND, forming a circuit
// This causes arduino to read a 1
// When the button is pressed, the signal is "rerouted" to the external GND and the arduino reads a 0
// This "rerouting" occurs due to a resistor with a very large resistance in the arduino internally
// Like a NOT gate
// (I believe)

int baudRate = 9600;
int dt = 100;

void setup() {
  Serial.begin(baudRate);

  pinMode(buttonPin, INPUT);

  digitalWrite(buttonPin, HIGH);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  Serial.print("Button State: ");
  Serial.println(buttonState);

  delay(dt);
}
