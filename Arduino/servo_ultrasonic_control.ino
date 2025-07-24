#include <Servo.h>
Servo servo1;
Servo servo2;
int trigPin = 9;
int echoPin = 10;
void setup() {
  Serial.begin(9600);
  servo1.attach(6);
  servo2.attach(7);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  digitalWrite(trigPin, LOW); delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10); digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;
  Serial.println(distance);
  if (distance < 10) {
    servo1.write(90); servo2.write(90);
  } else {
    servo1.write(0); servo2.write(0);
  }
  delay(100);
}