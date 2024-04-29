const int trigPin = 2;
const int echoPin = 3;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long czasTrwania = pomiarOdleglosci();
  float odleglosc = czasDoOdleglosci(czasTrwania);
  Serial.print("Odleglosc: ");
  Serial.print(odleglosc);
  Serial.println(" cm");
  delay(1000); // opóźnienie między pomiarami
}

long pomiarOdleglosci() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  return pulseIn(echoPin, HIGH);
}

float czasDoOdleglosci(long czas) {
  return static_cast<float>(czas) / 58.0f;
}