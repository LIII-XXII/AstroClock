# AstroClock

A clock that points at a satellite! Build your own International Space Station tracker. Never miss a visible pass again!

You need:
- a Raspberry Pi
  - we are using a Pi Zero because it is low power, but any model should work
  - https://www.raspberrypi.org/
- a stepper motor
  - smaller looks better, it just needs to move the clock hand
  - we are using a Tamagawa TS3692N65 (200 steps per revolution) but any NEMA stepper is fine.
  - the number of steps per revolution needs to be adjusted for different models
- a servo motor
  - again, smaller looks better
  - we are using a Tower Pro SG92R
  - the duty cycle will need to be adjusted for different models
- a stepper motor driver board
  - it supports microstepping, but we currently do not use the feature
  - we are using an EasyDriver and recommend supporting the designer by buying a board from them
  - http://www.schmalzhaus.com/EasyDriver/index.html

## Feature wishlist / TODO list

- add some kind of alert for when the satellite rises above the horizon and it may be visible
  - sound?
  - LED?

- detect if the object is visible with the naked eye (afaik it needs to be out of the Earth's shadow)

- track the Sun and turn it into a universal time clock (on servo axis) and a season clock (on stepper axis)

- automagically make it detect its own location

- add BOM

- add 3D printable parts
  - parametric OpenSCAD?

- unit tests for the `Stepper` class

## Troubleshooting

- numpy 1.14.3 can't open libf77blas.so.3 on Raspberry Pi Zero W (arm6)

you need to remove the numpy wheel package and get it from the raspbian repos instead:

```
pip3 uninstall numpy #remove previously installed package
apt install python3-numpy
```

more details at https://github.com/numpy/numpy/issues/11110#issuecomment-460026078
