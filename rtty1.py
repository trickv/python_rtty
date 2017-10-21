#!/usr/bin/env python3

import wiringpi
import time

wiringpi.wiringPiSetupGpio()

red_pin = 4
green_pin = 17
enable_pin = 23
txd_pin = 18
use_pwm = False # if yours sucks like mine

wiringpi.pinMode(red_pin, 1) # mode output
wiringpi.pinMode(green_pin, 1) # mode output
wiringpi.pinMode(enable_pin, 1) # mode output
wiringpi.digitalWrite(enable_pin,1)
if use_pwm:
    wiringpi.pinMode(txd_pin, 2) # PWM is only on GPIO pin 18
else:
    wiringpi.pinMode(txd_pin, 1) # regular GPIO mode, needs a resistor to get shift down to a decent width

baud = 50
baud_delay = 1.0/baud


def send_bit(value):
    if value < 0 or value > 1 or not type(value) is int:
        raise Exception("Invalid bit: %s" % value)
    if use_pwm:
        shift = 70 if value == 1 else 0
    else:
        shift = 1 if value == 1 else 0
    print("Sending bit %s with shift %d" % (value, shift))
    pin = green_pin if value else red_pin
    if use_pwm:
        wiringpi.pwmWrite(txd_pin, shift)
    else:
        wiringpi.digitalWrite(txd_pin, shift)
    #wiringpi.digitalWrite(pin, 1)
    time.sleep(baud_delay)
    #time.sleep(5)
    #wiringpi.digitalWrite(pin, 0)

def string_to_bit_strings(string):
    return [bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string]


def transmit(message):
    for character in string_to_bit_strings(message):
        print(character)
        send_bit(0)
        for bit in character[::-1]: # transmit bits from right to left
            send_bit(int(bit))
        send_bit(1)
        send_bit(1)

while True:
    transmit("Happy 30th Birthday, Sarah!\n")
    time.sleep(0.5)
