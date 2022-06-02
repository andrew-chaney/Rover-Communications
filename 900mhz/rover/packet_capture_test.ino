int packet_count;

void setup() {
    Serial.begin(9600);    // Computer connection
    Serial1.begin(57600);  // Radio connection
    Serial.print("Beginning packet capture...\n");
}

void loop() {
    int bytes_read = 0;
    byte packet[10] = {};

    // Capture the whole transmission.
    while (bytes_read < 10) {
      if (Serial1.available()) {
        packet[bytes_read++] = Serial1.read();
      }
    }

    Serial.print("Packet ");
    Serial.print(++packet_count);
    Serial.print(": ");
    for (int i = 0; i < 10; i++) {
      Serial.print(packet[i], HEX);
      Serial.print(' ');
    }
    Serial.print('\n');

    if ((int) packet[0] == 0 && (int) packet[9] == 1) {
        // If header and footer are valid, save the transmission contents for
        // use without the header and footer.
        byte stripped_packet[8] = {};
        for (int i = 1; i < 9; i++) {
            stripped_packet[i - 1] = packet[i];
        }

        Serial.print("Stripped Packet ");
        Serial.print(packet_count);
        Serial.print(": ");
        for (int i = 0; i < 8; i++) {
          Serial.print(stripped_packet[i], HEX);
          Serial.print(' ');
        }
        Serial.print('\n');
    }
}
