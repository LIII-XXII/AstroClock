#!/usr/bin/env python3
"""test the stepper by making it turn"""

from time import sleep

import gpiozero

STEP = gpiozero.OutputDevice(20)
DIR = gpiozero.OutputDevice(21)

STEPPER_RESOLUTION = 200  # 1.8deg per step
MICROSTEPS = 8

print('start!')
# full revolution
for i in range(STEPPER_RESOLUTION * MICROSTEPS):
    STEP.toggle()
    sleep(1 / 1000)
    STEP.toggle()
    sleep(1 / 1000)
