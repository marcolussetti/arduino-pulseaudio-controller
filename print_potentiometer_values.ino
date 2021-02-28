int const potOnePin = A0;
int const potTwoPin = A1;
int const potThreePin = A2;
int potOneVal;
int potTwoVal;
int potThreeVal;

void setup() {
  Serial.begin(9600);
  Serial.print("Started");
}

void loop() {
  // potOne
  potOneVal = analogRead(potOnePin);
  Serial.print("potOne=");
  Serial.print(potOneVal);
  Serial.print("\n");

  // potTwo
  potTwoVal = analogRead(potTwoPin);
  Serial.print("potTwo=");
  Serial.print(potTwoVal);
  Serial.print("\n");

  // potThree
  potThreeVal = analogRead(potThreePin);
  Serial.print("potThree=");
  Serial.print(potThreeVal);
  Serial.print("\n");

  delay(500);
}