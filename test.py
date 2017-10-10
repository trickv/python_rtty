#!/usr/bin/env python3

import wiringpi
import time

wiringpi.wiringPiSetupGpio()

red_pin = 4
green_pin = 17
enable_pin = 23
txd_pin = 18
wiringpi.pinMode(red_pin, 1) # mode output
wiringpi.pinMode(green_pin, 1) # mode output
wiringpi.pinMode(enable_pin, 1) # mode output
wiringpi.pinMode(txd_pin, 2) # PWM only on pin 18?
wiringpi.digitalWrite(enable_pin,1)

while True:
    #wiringpi.digitalWrite(red_pin,1)
    #wiringpi.digitalWrite(green_pin,0)
    wiringpi.pwmWrite(txd_pin, 200)
    time.sleep(50/1000)
    #wiringpi.digitalWrite(red_pin,0)
    #wiringpi.digitalWrite(green_pin,1)
    wiringpi.pwmWrite(txd_pin, 0)
    time.sleep(50/1000)

