#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Objects
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the sensors
left_color_sensor = ColorSensor(Port.S4)
right_color_sensor = ColorSensor(Port.S1)

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 20
GREEN = 20
BLUE = 40

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

# Fargesensor ting
def is_black(color_sensor):
    (red, green, blue) = color_sensor.rgb()
    return red < RED and green < GREEN and blue < BLUE

def follow_track(rotation):
    left_is_black = is_black(left_color_sensor)
    right_is_black = is_black(right_color_sensor)
    
    if left_is_black == right_is_black:
        rotation = 0
    elif left_is_black:
        rotation -= 2
        ev3.screen.print("Venstre er svart")
    else:
        rotation += 2
        ev3.screen.print("Høyre er svart")
    
    robot.drive(100, rotation)
    return rotation

rotation = 0
while True:
    rotation = follow_track(rotation)