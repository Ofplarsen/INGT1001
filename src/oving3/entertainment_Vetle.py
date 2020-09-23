#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
small_motor = Motor(Port.D)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

def entertainment_vetle():
    small_motor.run(1000)
    notes = list()
    for i in range(2, 8):
        for n in ["G", "F", "E", "D", "C", "B", "A"]:
            notes.append(n + str(i) + "/8")
    ev3.speaker.set_volume(100)
    ev3.speaker.play_notes(notes, tempo=120)
    small_motor.stop()

entertainment_vetle()