#!/usr/bin/env pybricks-micropython
from the color-sensor can have for the color to be defined as black
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random
import time

# Objects
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the sensors
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 50
GREEN = 50
BLUE = 50

# Get the percentage of red, green, and blue color from the color-sensor
(red, green, blue) = color_sensor.rgb()

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

def entertainment1():
    pass

def entertainment2():
    pass

def entertainment3():
    pass

def entertainment4():
    pass

def do_random_entertainment():
    entertainments = [entertainment1, entertainment2, entertainment3, entertainment4]
    random.choice(entertainments)()


def play_sound():
    pass


def follow_track():
    pass

def is_black():
    RED = 50
    GREEN = 50
    BLUE = 50
    (red, green, blue) = color_sensor.rgb()
    return red < RED or green < GREEN or blue < BLUE

while True:
    current_time = time.time()
    if current_time - last_time >= 10:
        do_random_entertainment()
        last_time = time.time()
    elif ultrasonic_sensor.distance() <= 200:
        robot.stop()
        play_sound()
    else:
        follow_track()
