#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 20
GREEN = 20
BLUE = 40

MAX_SPEED = 250
MIN_SPEED = 100

MAX_ROTATION_SPEED = 100

ACCELERATION = 1
ROTATION_ACCELERATION = 5

class RallyCar:    
    # Objects
    ev3 = EV3Brick()

    # Initialize the motors
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    # Initialize the sensors
    on_line_color_sensor = ColorSensor(Port.S4)
    off_line_color_sensor = ColorSensor(Port.S1)

    touch_sensor = TouchSensor(Port.S2)

    # Initialize the drive base.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

    speed = MAX_SPEED / 2
    rotation_speed = 0

    left_is_on_line = True
    ev3.screen.clear()
    ev3.screen.print("Mot klokka")

    def swap_color_sensors(self):
        temp = self.on_line_color_sensor
        self.on_line_color_sensor = self.off_line_color_sensor
        self.off_line_color_sensor = temp

    # Fargesensor ting
    def is_black(self, color_sensor):
        (red, green, blue) = color_sensor.rgb()
        return red < RED and green < GREEN and blue < BLUE

    def follow_track(self):
        on_line_is_black = self.is_black(self.on_line_color_sensor)
        off_line_is_black = self.is_black(self.off_line_color_sensor)
        
        if on_line_is_black:
            self.speed = min(self.speed + ACCELERATION, MAX_SPEED)
            self.rotation_speed = 0

        elif off_line_is_black == self.left_is_on_line:
            self.speed = max(self.speed - ACCELERATION, MIN_SPEED)
            self.rotation_speed = max(self.rotation_speed, 0)
            self.rotation_speed += ROTATION_ACCELERATION
            self.rotation_speed = min(self.rotation_speed, MAX_ROTATION_SPEED)

        else:
            self.speed = max(self.speed - ACCELERATION, MIN_SPEED)
            self.rotation_speed = min(self.rotation_speed, 0)
            self.rotation_speed -= ROTATION_ACCELERATION
            self.rotation_speed = max(self.rotation_speed, -MAX_ROTATION_SPEED)

        self.robot.drive(self.speed, self.rotation_speed)

        if self.touch_sensor.pressed():
            self.left_is_on_line = not self.left_is_on_line
            self.swap_color_sensors()
            self.ev3.screen.clear()
            if self.left_is_on_line:
                self.ev3.screen.print("Mot klokka")
            else:
                self.ev3.screen.print("Med klokka")

rally_car = RallyCar()
while True:
    rally_car.follow_track()