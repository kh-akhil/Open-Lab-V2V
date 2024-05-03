#include <SPI.h>
#include <LoRa.h> 
#define rst 9
#define ss 10
#define dia0 2

String inString = "";    // string to hold input
int val = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("LoRa Receiver");
  LoRa.setPins(ss, rst, dia0);
  if (!LoRa.begin(433E6)) { // or 915E6
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}
 
void loop() {
  
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  Serial.println(packetSize);
  if (packetSize) { 
    // read packet    
    while (LoRa.available())
    {
      int inChar = LoRa.read();
      Serial.println("inChar : ");
      Serial.println(inChar);
      inString += (char)inChar;
      val = inString.toInt();       
    }
    inString = "";     
    LoRa.packetRssi();    
  }
  Serial.println("Value : ");
  Serial.println(val);  
  Serial.println("----------------------------------------");
  delay(2000);
}