from registerClass import shiftRegister
import signal

shiftRegister = shiftRegister(1, 2, 3)

def signal_handler(signal, frame):
    global quit
    quit = True

signal.signal(signal.SIGINT, signal_handler)

quit = False
digitMap = {
    "0": 0b11111100,
    "1": 0b01100000,
    "2": 0b11011010,
    "3": 0b11110010,
    "4": 0b01100110,
    "5": 0b10110110,
    "6": 0b10111110,
    "7": 0b11100000,
    "8": 0b11111110,
    "9": 0b11110110,
    "a": 0b11101110,
    "b": 0b00111110,
    "c": 0b10011100,
    "d": 0b01111010,
    "e": 0b10011110,
    "f": 0b10001110,
    "-": 0b00000010,
    ".": 0b00000001,
    "all": 0b11111111,
    "off": 0b00000000
}

value = digitMap["off"]
while True:
    bytestring = format(value, '08b')
    shiftRegister.outputBits(bytestring)

    digit = raw_input("[0-9,a-f,-,.,all,off]: ")

    if digit == 'q':
        quit = True

    if quit:
        shiftRegister.clear()
        break

    value = digitMap.get(digit, value)
