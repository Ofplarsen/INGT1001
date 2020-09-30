#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

import random
import time

# Record time
last_time = time.time()

# Objects
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the sensors
color_sensor_1 = ColorSensor(Port.S1)
color_sensor_2 = ColorSensor(Port.S4)

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 10
GREEN = 10
BLUE = 10

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

# Fargesensor ting


def is_black(sensor):
    (red, green, blue) = sensor.rgb()
    return red < RED and green < GREEN and blue < BLUE


def play_sound():
    ev3.speaker.play_file(SoundFile.FANFARE)


rotation = 0
def follow_track():
    if is_black(color_sensor_1):
        ev3.screen.print("SENSOR 1 TRIGGERED")
        rotaio

    elif is_black(color_sensor_2):
        ev3.screen.print("SENSOR 2 TRIGGERED")
        robot.turn(2)

    else:
        robot.drive(1000, 0)


while True:
    current_time = time.time()
    follow_track()
