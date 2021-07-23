# Rules:------------------------------------------------------------------------------------

# Pygame module to play audio
# Assume that a programmer works at the office from 9am-5 pm. We have to take care of
# his health and remind him three things,
#
# To drink a total of 3.5-liter water after some time interval between 9-5 pm.
# To do eye exercise after every 30 minutes.
# To perform physical activity after every 45 minutes.

# Instructions:------------------------------------------------------------------------------

# The task is to create a program that plays mp3 audio until the programmer enters the
# input which implies that he has done the task.
#
# For Water, the user should enter “Drank”
# For Eye Exercise, the user should enter “EyDone”
# For Physical Exercise, the user should enter “ExDone”
# After the user enters the input, a file should be created for every task separately,
# which contains the details about the time when the user performed a certain task.

# Challenge:-----------------------------------------------------------------------------------

# You will have to manage the clashes between the reminders such that no two
# reminders play at the same time.
# Use pygame module to play audio.

# Healthy Programmer:----------------------------------------------------------------------

# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log

from pygame import mixer
from datetime import datetime
from time import time


def music_on_loop(file, stopper):
    """
    this function will keep on playing music until stopper argument is passed..
    """
    mixer.init()  # init will initialize the mixer func from pygame module, which is used to play audiofile
    mixer.music.load(file)
    mixer.music.play()
    while True:  # this loop is for continuous play of music till the user enter the stopper argument
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    """
    this func will create a log file which will contain the data of when you have taken water, done
    exercise, relaxed your eyes

    """
    with open("log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == "__main__":
    init_water = time()  # these variables  will keep the time of when the program started..
    init_eyes = time()
    init_exercise = time()
    # water_secs, eyes_secs, exer_secs are the interval timing in minutes
    water_secs = 30*60  # change these according to your timing
    eyes_secs = 20*60
    exer_secs = 60*60

    while True:

        if time() - init_water > water_secs:  # this will give the 'interval' time..
            print("water drinking time---"
                  "enter  'drank' to stop the alarm")
            music_on_loop("water.mp3", "drank")
            init_water = time()  # here the init_water will be having starting time for the
            # next interval of the drinking water
            log_now("Drank water at:-  ")

        if time() - init_eyes > eyes_secs:
            print("Time for eye relaxation:- "
                  "ENTER 'done' to stop the alarm ")
            music_on_loop("water.mp3", "done")
            init_eyes = time()  # same as above described for the init_water variable
            log_now("Time at which eyes relaxed:- ")

        if time() - init_exercise > exer_secs:
            print("Time for physical activity:- "
                  "ENTER 'donephy' to stop the alarm ")
            music_on_loop("water.mp3", "donephy")
            init_exercise = time()  # same as above described for the init_water variable
            log_now("Time at which physical activity done:- ")
