import hid

def main():
    for device in hid.enumerate():
        print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

    controller = hid.device()
    controller.open(0x046d, 0xc216)
    controller.set_nonblocking(True)
    
    while True:
        report = controller.read(64)
        if report:
            print(report)


if __name__ == "__main__":
    main()