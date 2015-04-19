long velocityInput = 25; 
float rpm = 300.0;
long duty = 12;

void setup(){
// Open serial connection.
Serial.begin(9600);
 
}
 
void loop(){
  Serial.print(velocityInput);
  Serial.print(" ");
  Serial.print(rpm);
  Serial.print(" ");
  Serial.println(duty);
  delay(10); // ms
}
