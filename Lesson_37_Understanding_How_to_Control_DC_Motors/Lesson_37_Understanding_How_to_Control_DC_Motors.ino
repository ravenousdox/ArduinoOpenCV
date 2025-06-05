// Lesson 37 Understanding How to Control DC Motors
// Power supply, L293D Motor Controller, Servo Motor
// Turning off servo motors produces huge voltage spikes which can be sent back to the arduino, frying it
// This is due to the inductance and the time it takes to chane the current in the wire coils
// You could use a transistor and a diode with reverse bias to control the servo with the arduino safely but motor controllers are now more commonly used
// The L293D can control up to two motors

// Pin 1 -> EN1  (Controls speed of motor, accepts an analog value (PWM ~ Pin on arduino))
// Pin 2 -> IN1  (Controls direction of rotation along with Pin 7, Counter Clockwise)
// Pin 3 -> OUT1 (Red pin of motor goes here)
// Pin 4 -> 0V   (Connects to common ground, negative rail)
// Pin 5 -> 0V
// Pin 6 -> OUT2 (Black pin of motor goes here)
// Pin 7 -> IN2  (Clockwise)
// Pin 8 -> +Vmotor (Goes to VCC of power supply, positive rail)

int speedPin = 5;
int forwardPin = 4;
int backwardPin = 3;

// The smallest speed my DC motor can operate at
int motorSpeed = 100;

int fiveSeconds = 5000;

void setup() {
  Serial.begin(baudRate);
  
  pinMode(speedPin, OUTPUT);
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);

}

void loop() {
  digitalWrite(forwardPin, HIGH);
  digitalWrite(backwardPin, LOW);
  analogWrite(speedPin, 255);
  delay(25);
  analogWrite(speedPin, motorSpeed);
  delay(fiveSeconds);
}
