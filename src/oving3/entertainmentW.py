#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random
import time

ev3.screen.clear()
ev3.screen.draw_text(20, 250, 'Bad time xd', text_color = Color.BLACK, background_color = None)
ev3.screen.clear()
ev3.speaker.play_notes('D4/_', 'D4/_', 'D4/5', tempo = 120)
#ev3.speaker.play_notes('D4/_', 'D4/_', 'D4/5', 'D4/4.', 'A4/4', 'G#4/4', 'G4/4', 'F4/4', 'D4/_', 'F4/_', 'G4/_', tempo = 120)
