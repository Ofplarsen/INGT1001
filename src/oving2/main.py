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
ultrasonicS = UltrasonicSensor(Port.S2)
touchS = TouchSensor(Port.S1)

#Code
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

isOn = False

def bigBeeper():
    ev3.speaker.set_volume(30)
    ev3.speaker.beep()
    ev3.speaker.set_volume(10)

def smallBeeper():
    ev3.speaker.set_volume(10)
    ev3.speaker.beep()

bigBeeper()
while True:
    if touchS.pressed():
            ev3.screen.print(isOn)
            isOn = True
            bigBeeper()
    while isOn:
        while ultrasonicS.distance() > 100:
            robot.drive(50,0)
            if touchS.pressed():
                ev3.screen.print(isOn)
                isOn = False
                bigBeeper()
                break
            
        robot.turn(20)
        robot.straight(-75)