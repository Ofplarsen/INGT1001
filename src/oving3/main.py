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
small_motor = Motor(Port.D)

# Initialize the sensors
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Global variables that defines the maximum RGB-values a sensor-reading
RED = 50
GREEN = 50
BLUE = 50

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=138)

# Fargesensor ting
def is_black():
    (red, green, blue) = color_sensor.rgb()
    return red < RED and green < GREEN and blue < BLUE

def entertainment1(): # Vetle
    small_motor.run(1000)
    notes = list()
    for i in range(2, 8):
        for n in ["G", "F", "E", "D", "C", "B", "A"]:
            notes.append(n + str(i) + "/8")
    ev3.speaker.set_volume(100)
    ev3.speaker.play_notes(notes, tempo=120)
    small_motor.stop()

def entertainment2(): # Olav
    ev3.screen.clear()
    ev3.screen.load_image("ent_olav.png")
    ev3.speaker.say("Love yourself")
    time.sleep(5)
    ev3.screen.clear()

def entertainment3(): # William
    ev3.screen.clear()
    ev3.screen.draw_text(20, 250, 'Bad time xd', text_color = Color.BLACK, background_color = None)
    ev3.screen.clear()
    ev3.speaker.play_notes(['D4/4', 'D4/4', 'D5/4', 'D4/4.', 'A4/4', 'G#4/4', 'G4/4', 'F4/4', 'D4/4_', 'F4/4_', 'G4/4_'], tempo = 400)

def entertainment4():
    ev3.speaker.set_volume(100)
    ev3.screen.clear()
    ev3.screen.print("Obama Chicken")
    ev3.speaker.say("Hello, I am President Obama.")
    ev3.speaker.play_notes(['C5/4','E5/4.','A5/4', 'C5/4', 'C5/4','R/4', 'E5/4', 'A5/4', 'E5/4', 'B4/4','E5/4','A5/4','B4/4','R/4','E5/4','G5/4','E5/4','C5/4','E5/4'], 250)
    ev3.screen.clear()


def do_random_entertainment():
    entertainments = [entertainment1, entertainment2, entertainment3, entertainment4]
    random.choice(entertainments)()


def play_sound():
    ev3.speaker.play_file(SoundFile.FANFARE)


def follow_track():  
    if is_black():
        ev3.screen.print("DRIVING")
        robot.drive(50, 0)

    else:
        ev3.screen.print("TURNING")
        robot.turn(-2)

while True:
    current_time = time.time()

    if ultrasonic_sensor.distance() <= 200:
        robot.stop()
        play_sound()

    elif current_time - last_time >= 10:
        robot.stop()
        do_random_entertainment()
        last_time = time.time()
        
    else:
        follow_track()
