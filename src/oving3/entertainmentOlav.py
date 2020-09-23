import random


def do_random_entertainment():
    randomNum = random.randint(0, 3)
    if (randomNum == 0):
        entertainment1()
    elif (randomNum == 1):
        entertainment2()
    elif (randomNum == 2):
        entertainment3()
    elif (randomNum == 3):
        entertainment4()
