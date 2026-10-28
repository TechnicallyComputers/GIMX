import serial

PORT = "/dev/ttyUSB0"
BAUD = 500000

with serial.Serial(PORT, BAUD, timeout=2) as ser:
    ser.reset_input_buffer()
    ser.write(bytes([0x78, 0x00]))

    response = ser.read(9)

    if len(response) != 9:
        print(f"Incomplete response: {response.hex(' ')}")
    elif response[0] != 0x78 or response[1] != 7:
        print(f"Unexpected response: {response.hex(' ')}")
    else:
        print("Reset reason:", response[2])
        print("Packet type:", hex(response[3]))
        print("Expected length:", response[4])
        print("Received length:", response[5])
        print("MCUSR flags:", hex(response[6]))
        print("Reset count:", int.from_bytes(response[7:9], "little"))
