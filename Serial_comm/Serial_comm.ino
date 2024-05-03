#include <SPI.h>
#include <LoRa.h> 
#define rst 9
#define ss 10
#define dia0 2
int count = 0;
String inString = "";    // string to hold input
int val1 = 0;
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
  char val[] ="1,77.631054,13.026446";
  if (count <= 0){
    Serial.println(val);
  }
  int packetSize = LoRa.parsePacket();
  if (packetSize) {    
    while (LoRa.available())
    {
      int inChar = LoRa.read();
      Serial.println("inChar : ");
      Serial.println(inChar);
      inString += (char)inChar;
      val1 = inString.toInt();       
    }
    inString = "";     
    LoRa.packetRssi();    
  }
  delay(2000);
}
