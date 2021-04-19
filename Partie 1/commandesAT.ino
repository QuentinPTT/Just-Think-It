#include <SoftwareSerial.h>

SoftwareSerial hc05(10, 11);
    
void setup() {
  // Initialiser le Serial Monitor
  Serial.begin(115200);
  Serial.println("Commandes AT:");
  // Initialiser le port Bluetooth
  hc05.begin(9600);
}
    
void loop() {
  // Transferer les donnees du HC05 vers le SM
  if (hc05.available()) {
   Serial.write(hc05.read());
  }
}
  
