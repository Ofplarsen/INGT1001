#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
small_motor = Motor(Port.D)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

ev3.speaker.set.volume(100)

ev3.screen.clear()
ev3.screen.print("Obama Chicken")
ev3.speaker.say("Hello, I am President Obama.")
ev3.play.notes(['C4_','C4_','G4.'], 90)
ev3.small_motor.run(30)
wait(2000)
ev3.screen.clear()