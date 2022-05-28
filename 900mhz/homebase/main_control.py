import hid
import logging
import serial
import sys
import time

def setup_logger(verbose=False):
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")
    
    file_handler = logging.FileHandler("transmissions.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)


def get_controller():
    global controller
    VID = 0x046d
    PID = 0xc216
    controller = hid.device()
    controller.open(VID, PID)
    controller.set_nonblocking(True)


def write_to_stream(x) -> bytearray:
    data = bytearray(x)
    Serial.write(data)
    time.sleep(0.05)
    return data


def main():
    global Serial

    setup_logger(verbose=True)

    logger.debug("Attempting serial connection.")
    Serial = serial.Serial(
        port="/dev/tty.usbserial-AB0KTHBP",
        baudrate="57600",
        timeout=.1
    )
    logger.debug("Serial connection successful.")
    
    logger.debug("Attempting controller connection.")
    get_controller()
    logger.debug("Controller connection successful.")

    
    packets_sent = 0
    logger.debug("Listening for input to transmit.")
    while True:
        output = controller.read(64)
        if output:
            data = write_to_stream(output)
            packets_sent += 1
            logger.debug("PACKET {} TRANSMITTED --- Packet Data: [{}]".format(
                packets_sent,
                " ".join(["{:02x}".format(x) for x in data])
            ))


if __name__ == "__main__":
    main()