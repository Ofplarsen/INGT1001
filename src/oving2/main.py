#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Objects
ev3 = EV3Brick()
ultrasonic = UltrasonicSensor(Port.S2)
touch = TouchSensor(Port.S1)

#Code
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

ev3.speaker.set_volume(50)
ev3.speaker.beep()
ev3.speaker.set_volume(10)


while True:
    if touch.pressed():
        ev3.speaker.set_volume(50)
        ev3.speaker.beep()
        exit()
    while ultrasonic.distance() > 100:
        robot.drive(50,0)
    robot.drive(-50,0)
    robot.turn(20)
    wait(10)