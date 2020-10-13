#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 20
GREEN = 20
BLUE = 40

STRAIGHT_SPEED = 100
SWING_SPEED = 50
SWING_ROTATION = 2

class RallyCar:    
    # Objects
    ev3 = EV3Brick()

    # Initialize the motors
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    # Initialize the sensors
    left_color_sensor = ColorSensor(Port.S4)
    right_color_sensor = ColorSensor(Port.S1)

    # Initialize the drive base.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

    speed = STRAIGHT_SPEED
    rotation = 0
    left_time = None
    right_time = None

    # Fargesensor ting
    def is_black(self, color_sensor):
        (red, green, blue) = color_sensor.rgb()
        return red < RED and green < GREEN and blue < BLUE

    def cross_intersection(self):
        self.robot.stop()
        self.robot.straight(100)

        angle = 0
        if self.left_time < self.right_time:
            angle = 2 # Turn right
        else:
            angle = -2 # Turn left

        while not self.is_black(self.left_color_sensor) and not self.is_black(self.right_color_sensor):
            self.robot.turn(angle)

        while self.is_black(self.left_color_sensor) or self.is_black(self.right_color_sensor):
            self.robot.turn(angle)

        self.rotation = 0
        self.left_time = None
        self.right_time = None

    def is_at_intersection(self):
        if self.left_time == None or self.right_time == None:
            return False
        else:
            return abs(self.left_time - self.right_time) < 0.5

    # Ta sensorene lengre fra hverandre?

    def follow_track(self):
        left_is_black = self.is_black(self.left_color_sensor)
        right_is_black = self.is_black(self.right_color_sensor)
        
        if left_is_black == right_is_black:
            self.rotation = 0
            self.speed = STRAIGHT_SPEED
            
        if left_is_black:
            self.rotation -= SWING_ROTATION
            self.speed = SWING_SPEED
            self.left_time = time.time()

        if right_is_black:
            self.rotation += SWING_ROTATION
            self.speed = SWING_SPEED
            self.right_time = time.time()

        if self.is_at_intersection():
            self.cross_intersection()
        else:
            self.robot.drive(self.speed, self.rotation)

rally_car = RallyCar()
while True:
    rally_car.follow_track()