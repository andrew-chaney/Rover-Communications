import hid

VID = 0x046d
PID = 0xc216

def main():
    path = ""
    for device in hid.enumerate():
        print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")
        if device['vendor_id'] == VID and device['product_id'] == PID:
            path = device['path']
    
    print()
    print(path)
    print()

    controller = hid.device()
    controller.open(VID, PID)
    controller.set_nonblocking(1)
    
    while True:
        report = controller.read(64)
        if report:
            print(report)


if __name__ == "__main__":
    main()