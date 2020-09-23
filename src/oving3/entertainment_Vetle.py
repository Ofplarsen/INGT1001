ev3 = EV3Brick()
small_motor = Motor(Port.D)

def entertainment_vetle():
    small_motor.run(1000)
    notes = list()
    for i in range(2, 9):
        for n in ['G', 'F', 'E', 'D', 'C', 'B', 'A']:
            notes.append(n + str(n) + '/8')
    ev3.speaker.set_volume(100)
    ev3.speaker.bee.play_notes(notes, tempo=120)
    small_motor.stop()