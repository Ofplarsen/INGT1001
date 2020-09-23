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


class EV3_devices:
    def __init__(self, robot=None, touch_sensor=None, color_sensor=None, infrared_sensor=None, ultrasonic_sensor=None, gyroscopic_sensor=None):
        self.robot = robot
        self.touch_sensor = touch_sensor
        self.color_sensor = color_sensor
        self.infrared_sensor = infrared_sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        self.gyroscopic_sensor = gyroscopic_sensor


ev3_devices = EV3_devices(
    robot=robot, color_sensor=color_sensor, ultrasonic_sensor=ultrasonic_sensor)


def entertainment1(ev3_devices):
    pass


def entertainment2(ev3_devices):
    pass


def entertainment3(ev3_devices):
    pass


def entertainment4(ev3_devices):
    pass


def do_random_entertainment(ev3_devices):
    entertainments = [entertainment1, entertainment2,
                      entertainment3, entertainment4]
    random.choice(entertainments)(ev3_devices)


def play_sound():
    pass


def follow_track():
    pass


while True:
    current_time = time.time()
    if current_time - last_time >= 10:
        do_random_entertainment(ev3_devices)
        last_time = time.time()
    elif ultrasonic_sensor.distance() <= 200:
        robot.stop()
        play_sound()
    else:
        follow_track()
