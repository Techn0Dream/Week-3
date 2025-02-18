#include <Arduino_LSM6DS3.h>

void setup() {
    Serial.begin(115200);
    while (!Serial); // Wait for serial connection

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
    Serial.println("Timestamp,X,Y,Z"); // CSV header
}

void loop() {
    float x, y, z;

    if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);
        
        // Get current timestamp
        unsigned long timestamp = millis();
        
        // Print data in CSV format
        Serial.print(timestamp);
        Serial.print(",");
        Serial.print(x, 6);
        Serial.print(",");
        Serial.print(y, 6);
        Serial.print(",");
        Serial.println(z, 6);
    }
    
    delay(1000); // 1 sample per second
}
