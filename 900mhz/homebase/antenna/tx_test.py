import serial
import time

Serial = serial.Serial(
    port="/dev/tty.usbserial-AB0KTHBP",
    baudrate="57600",
    timeout=.1
)

def write_read(x):
    Serial.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = Serial.readline()
    return data

def main():
    while True:
        num = input(">> ")
        val = write_read(num)
        print(val)

if __name__ == "__main__":
    main()
