#!/usr/bin/env python3
"""test the servo by making it move"""

from time import sleep

import gpiozero

#min pulse 0.5 ms max pulse 2.4 ms
servo = gpiozero.Servo(16, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

print('start!')
while(True):
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
