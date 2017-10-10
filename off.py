#!/usr/bin/env python3

import wiringpi
import time

wiringpi.wiringPiSetupGpio()

enable_pin = 23
red_pin = 4
green_pin = 17
wiringpi.pinMode(enable_pin, 1) # mode output
wiringpi.pinMode(red_pin, 1) # mode output
wiringpi.pinMode(green_pin, 1) # mode output
wiringpi.digitalWrite(enable_pin,0)
wiringpi.digitalWrite(red_pin,0)
wiringpi.digitalWrite(green_pin,0)
