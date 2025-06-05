// Tutorial 29 Using Push Buttons to Create a Dimmable LED
// Uses two buttons 
// When the corresponding button is pressed/held, it increments/decrements the brightness of an LED
// If maximum/minimum brightness has already been reached, it activates a buzzer to notify the operator
// For good practice, put the serial output after the logic (Would this be good practice?)

int baudRate = 9600;
int dt = 250;
int brightButtonPin = 12;
int dimButtonPin = 11;
int ledPin = 3;               // A PWM pin that can be used for writing analog values
int buzzerPin = 2;

int brightButton, dimButton;  // Holds the state of the corresponding button
int brightness = 0;           // Brightness ranges in [0, 255]

void setup() {
  Serial.begin(baudRate);
  pinMode(brightButtonPin, INPUT);
  pinMode(dimButtonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Read the state of the buttons
  brightButton = digitalRead(brightButtonPin);
  dimButton = digitalRead(dimButtonPin);

  // Output the state of the buttons to the Serial Monitor
  Serial.println("Bright Button: ");
  Serial.print(brightButton);
  Serial.print(", ");
  Serial.print("Dim Button: ");
  Serial.print(dimButton);

  delay(dt);

  // If the button used to increase brightness is pressed
  // and is below the maximum brightness
  // increase the brightness by 5
  // Else if the maximum brightness has been reached
  // Sound the buzzer!
  if (!brightButton)
    if (brightness < 255)
      brightness += 5;
    else {
      digitalWrite(buzzerPin, HIGH);
      delay(dt);
      digitalWrite(buzzerPin, LOW);
    }

   if (!dimButton)
    if (brightness > 0)
      brightness -= 5;
    else {
      digitalWrite(buzzerPin, HIGH);
      delay(dt);
      digitalWrite(buzzerPin, LOW);
    }

   // Write the brightness value to the LED
   analogWrite(ledPin, brightness);

}
