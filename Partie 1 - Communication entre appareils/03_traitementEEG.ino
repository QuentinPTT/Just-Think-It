#define BAUDRATE 115200
#define DEBUGOUTPUT 0
#define EEG_POWER_BANDS 8

byte generatedChecksum = 0;
byte checksum = 0; 
int payloadLength = 0;
byte payloadData[64] = {0};
byte poorQuality = 0;
byte attention = 0;
byte meditation = 0;
uint32_t eegPower[EEG_POWER_BANDS];

long lastReceivedPacket = 0;
boolean bigPacket = false;
boolean hasPower = false;

void setup() {
  Serial.begin(BAUDRATE);

}

byte ReadOneByte() {
  int ByteRead;

  while(!Serial.available());
  ByteRead = Serial.read();

#if DEBUGOUTPUT  
  Serial.print((char)ByteRead);
#endif

  return ByteRead;
}

void loop() {


  // Look for sync bytes
  if(ReadOneByte() == 170) {
    if(ReadOneByte() == 170) {

      payloadLength = ReadOneByte();
      if(payloadLength > 169)                      
          return;

      generatedChecksum = 0;        
      for(int i = 0; i < payloadLength; i++) {  
        payloadData[i] = ReadOneByte();          
        generatedChecksum += payloadData[i];
      }   

      checksum = ReadOneByte();                          
      generatedChecksum = 255 - generatedChecksum;  
      
        if(checksum == generatedChecksum) {    

        poorQuality = 200;
        attention = 0;
        meditation = 0;

        for(int i = 0; i < payloadLength; i++) {
          switch (payloadData[i]) {
          case 2:
            i++;            
            poorQuality = payloadData[i];
            bigPacket = true;            
            break;
          case 4:
            i++;
            attention = payloadData[i];                        
            break;
          case 5:
            i++;
            meditation = payloadData[i];
            break;
          case 0x80:
            i = i + 3;
            break;
          case 0x83:
            for (int j = 0; j < EEG_POWER_BANDS; j++) {
                    eegPower[j] = ((uint32_t)payloadData[++i] << 16) | ((uint32_t)payloadData[++i] << 8) | (uint32_t)payloadData[++i];
                }
            hasPower = true;
            break;
          }
        }

#if !DEBUGOUTPUT

        if(bigPacket) {
          Serial.println("");
          Serial.println("--- Start Packet ---");
          Serial.print("Signal Quality: ");
          Serial.println(poorQuality, DEC);
          Serial.print("Attention: ");
          Serial.println(attention, DEC);Serial.print("Meditation: ");Serial.println(meditation, DEC);             
        }
        if (hasPower) {
            Serial.println("");
            Serial.println("EEG POWER:");
            Serial.print("Delta: ");
            Serial.println(eegPower[0], DEC);
            Serial.print("Theta: ");
            Serial.println(eegPower[1], DEC);
            Serial.print("Low Alpha: ");
            Serial.println(eegPower[2], DEC);
            Serial.print("High Alpha: ");
            Serial.println(eegPower[3], DEC);
            Serial.print("Low Beta: ");
            Serial.println(eegPower[4], DEC);
            Serial.print("High Beta: ");
            Serial.println(eegPower[5], DEC);
            Serial.print("Low Gamma: ");
            Serial.println(eegPower[6], DEC);
            Serial.print("Mid Gamma: ");
            Serial.println(eegPower[7], DEC);
        }
#endif        
        bigPacket = false;
        hasPower = false;        
      }
      else {
      }
    }
  }
}
