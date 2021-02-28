const int POTS = 3;
const int DELAY = 500;

int potPids[] = {A0, A1, A2};
int potVals[] = {0, 0, 0};

void setup() {
  Serial.begin(9600);
  Serial.print("Started");
}

void loop() {
  for (int i = 0; i < POTS; i++) {
    potVals[i] = analogRead(potPids[i]);
    Serial.print("pot");
    Serial.print(i);
    Serial.print("=");
    Serial.print(potsVals[i]);
    Serial.print("\n");
  }

  delay(DELAY);
}
