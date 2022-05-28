import hid
import serial
import time

def get_controller():
    c = hid.device()
    c.open(VID, PID)
    c.set_nonblocking(True)
    return c

def write_to_stream(x):
    data = bytearray(x)
    Serial.write(data)
    time.sleep(0.05)
    return data

def main():
    global VID, PID, Serial

    VID = 0x046d
    PID = 0xc216

    print("Initializing serial connection...", end='')
    Serial = serial.Serial(
        port="/dev/tty.usbserial-AB0KTHBP",
        baudrate="57600",
        timeout=.1
    )
    print("DONE")
    
    print("Initializing controller connection...", end='')
    controller = get_controller()
    print("DONE\n")
    
    packets_sent = 0

    while packets_sent < 50:
        output = controller.read(64)
        if output:
            data = write_to_stream(output)
            packets_sent += 1
            print(f"Packet {packets_sent}: {' '.join(['{:02x}'.format(x) for x in data])}")

    print(f"\nPackets Sent: {packets_sent}")

if __name__ == "__main__":
    main()