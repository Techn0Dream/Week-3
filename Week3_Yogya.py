import serial
import csv
import time
import matplotlib.pyplot as plt

SERIAL_PORT = "/dev/cu.usbmodem1101"  
BAUD_RATE = 115200
FILENAME = "accelerometer_data.csv"

# Open Serial Connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Give Arduino some time to start

# Open CSV File
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "X", "Y", "Z"])  # CSV Header
    
    try:
        print("Collecting data... Press CTRL+C to stop.")
        while True:
            line = ser.readline().decode().strip()
            if line and "Timestamp" not in line:  # Ignore header
                print(line)  # Print received data
                writer.writerow(line.split(","))  # Save to CSV
                
    except KeyboardInterrupt:
        print("\nData collection stopped.")
        ser.close()

# Plot Data
import pandas as pd

df = pd.read_csv(FILENAME)
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["X"], label="X-axis", color="red")
plt.plot(df["Timestamp"], df["Y"], label="Y-axis", color="green")
plt.plot(df["Timestamp"], df["Z"], label="Z-axis", color="blue")
plt.xlabel("Timestamp (ms)")
plt.ylabel("Acceleration (g)")
plt.legend()
plt.title("LSM6DS3 Accelerometer Data")
plt.grid()
plt.show()
