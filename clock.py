#!/usr/bin/env python3
"""points at a satellite in the sky"""

import logging
from time import sleep

from pytz import timezone
#import numpy

import gpiozero
from skyfield import api as skyfapi

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

UTC = timezone('UTC')
SATS = skyfapi.load.tle('https://celestrak.com/NORAD/elements/resource.txt')
SAT = SATS['HODOYOSHI-1']
TS = skyfapi.load.timescale()
TOKYO = skyfapi.Topos(latitude='35.688926 N', longitude='139.774214 W')
# min pulse 0.5 ms max pulse 2.4 ms
SERVO = gpiozero.Servo(
    16, min_pulse_width=0.5 / 1000, max_pulse_width=2.4 / 1000)


class Stepper:

    "Stepper motor helper class"

    STEPPER_RESOLUTION = 200  # 1.8deg per step
    MICROSTEPS = 8
    STEP = gpiozero.OutputDevice(20)
    DIR = gpiozero.OutputDevice(21)
    PERIOD = 1 / 2000  # bitbanged stepper STEP signal length

    current_step = 0
    current_direction_is_forward = True

    def getPos(self) -> int:
        return self.current_step

    def doStep(self):
        self.STEP.toggle()
        sleep(self.PERIOD)
        self.STEP.toggle()
        sleep(self.PERIOD)
        return

    def reverse(self) -> bool:
        self.DIR.toggle()
        self.current_direction_is_forward = not self.current_direction_is_forward
        return self.current_direction_is_forward

    def step(self, numsteps: int = 1) -> int:
        if numsteps < 0:
            self.reverse()

        for i in range(abs(int(numsteps))):
            self.doStep()

        if numsteps < 0:
            self.reverse()

        self.current_step += numsteps
        return self.current_step

    def getAngle(self) -> float:
        return self.step2deg(self.current_step)

    @staticmethod
    def step2deg(s: int) -> float:
        return s / Stepper.STEPPER_RESOLUTION / Stepper.MICROSTEPS * 360

    @staticmethod
    def deg2step(deg: float) -> int:
        return deg * Stepper.STEPPER_RESOLUTION * Stepper.MICROSTEPS / 360

    def go2step(self, toStep: int) -> int:
        return self.step(toStep - self.getPos())

    def go2angle(self, toAngle: float) -> int:
        """return number of stepped steps"""
        targetStep = int(self.deg2step(toAngle))
        if targetStep != self.getPos():
            logger.info('Stepping...')
            return self.go2step(targetStep)
        return 0

logger.info('Start!')

while True:
    azimuthStepper = Stepper()
    orbit = (SAT - TOKYO).at(TS.now())
    alt, az, distance = orbit.altaz()
    if azimuthStepper.go2angle(az.degrees):
        SERVO.value = alt.degrees / 90
        logger.debug('now pointing towards:', alt, az, distance.km)
