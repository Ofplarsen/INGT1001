#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image, empty

import random
import time

# Objects
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_arm = Motor(Port.D)

# Initialize the sensors
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

# Initialize the image

class EV3_devices:
    def __init__(self, robot = None, touch_sensor = None, color_sensor = None, infrared_sensor = None, ultrasonic_sensor = None, gyroscopic_sensor = None):
        self.robot = robot
        self.touch_sensor = touch_sensor
        self.color_sensor = color_sensor
        self.infrared_sensor = infrared_sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        self.gyroscopic_sensor = gyroscopic_sensor

ev3_devices = EV3_devices(robot=robot, color_sensor=color_sensor, ultrasonic_sensor=ultrasonic_sensor)

def entertainment_olav(ev3_devices):
    ev3.screen.clear()
    ev3.screen.Image("entOlav.png")
    motor_arm.run_time(100, 5, Stop.HOLD, False)
    ev3.speaker.say("Entertainment grrrrrrrr")
    time.sleep(5)
    ev3.screen.clear()
    

