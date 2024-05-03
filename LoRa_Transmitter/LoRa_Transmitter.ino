
#include <SPI.h>
#include <LoRa.h> 
#define rst 9
#define ss 10
#define dia0 2
void setup() {
  Serial.begin(9600);
  
  while (!Serial);  
  Serial.println("LoRa Sender");
  LoRa.setPins(ss, rst, dia0);
  if (!LoRa.begin(433E6)) { // or 915E6, the MHz speed of yout module
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}
 
void loop() {
  int val = 200;
  LoRa.beginPacket();  
  LoRa.print("hello");
  LoRa.endPacket();
  delay(50);
 
}