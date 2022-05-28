int packet_count;

void setup() {
  Serial.begin(9600);    // Computer connection
  Serial1.begin(57600);  // Radio connection
  Serial.print("Beginning packet capture...\n")
}

void loop() {
  int bytes_read = 0;
  byte packet[8] = {};
  
  while (bytes_read < 8) {
    if (Serial1.available()) {
      packet[bytes_read++] = Serial1.read();
    }
  }
  
  Serial.print("Packet ");
  Serial.print(++packet_count);
  Serial.print(": ");
  
  for (int i = 0; i < 8; i++) {
    Serial.print(packet[i], HEX);
    Serial.print(' ');
  }
  Serial.print('\n');
}