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

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the sensors
touch_sensor = TouchSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)


def wait_until_pressed(touch_sensor):
    while not touch_sensor.pressed():
        continue


def drive_until_pressed(robot, touch_sensor, ultrasonic_sensor):
    while not touch_sensor.pressed():
        if ultrasonic_sensor.distance() > 150:
            robot.drive(100, 0)
        else:
            robot.straight(-50)
            robot.turn(30)
    robot.stop()


while True:
    wait_until_pressed(touch_sensor)
    ev3.speaker.say("Exercise 2")
    drive_until_pressed(robot, touch_sensor, ultrasonic_sensor)
    ev3.speaker.say("Exercise done")
