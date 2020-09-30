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
left_color_sensor = ColorSensor(Port.S4)
right_color_sensor = ColorSensor(Port.S1)

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 25
GREEN = 25
BLUE = 25

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

# Fargesensor ting


def is_black(sensor):
    (red, green, blue) = sensor.rgb()
    return red < RED and green < GREEN and blue < BLUE


def play_sound():
    ev3.speaker.play_file(SoundFile.FANFARE)


def check_values(sensor):
    (red, green, blue) = sensor.rgb()
    ev3.screen.clear()

    ev3.screen.print("R: " + str(red))
    ev3.screen.print("G: " + str(green))
    ev3.screen.print("B: " + str(blue))


turnCounter = 0
speed = 0
rotation = 0


def follow_track():
    global turnCounter
    global speed
    global rotation

    left_is_black = is_black(left_color_sensor)
    right_is_black = is_black(right_color_sensor)

    if (not left_is_black and not right_is_black):
        ev3.screen.print("FORWARD")
        speed = 60
        rotation = 0
        turnCounter = 0

    elif left_is_black:
        ev3.screen.print(str(turnCounter))
        turnCounter += 1
        if (turnCounter < 30):
            speed = 30
            rotation = -5
            ev3.screen.print("LEFT:")
        else:
            speed = 10
            rotation = -15
            ev3.screen.print("HARD LEFT:")

    elif right_is_black:
        ev3.screen.print(str(turnCounter))
        turnCounter += 1
        if (turnCounter < 30):
            speed = 30
            rotation = 5
            ev3.screen.print("RIGHT:")
        else:
            speed = 10
            rotation = 15
            ev3.screen.print("HARD RIGHT:")

    robot.drive(speed, rotation)


while True:
    follow_track()
