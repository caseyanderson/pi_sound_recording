#!/usr/bin/python3

'''
toggle recording on/off via button press'''

from recorder import *
from gpiozero import Button
from gpiozero import LED
from datetime import datetime
from time import sleep

BASE_DIR = '/home/cta/'
NAME =  ''
FORMAT = '.wav'

input_pin = 4
is_recording = 0
duration = 0            # a duration of 0 results in "infinite" recording

button = Button(input_pin)
led = LED(17)

print("ready to record!")
try:
    while True:
        if is_recording == 0 and button.value == True:
            print('button pressed, setting up and starting recording')
            DATE = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
            FILENAME = ''.join([NAME, DATE, FORMAT])
            REC_PATH = ''.join([BASE_DIR, FILENAME])
            recorder = Recorder(REC_PATH, duration)
            sleep(0.5)              # unnecessary?
            recorder.record()
            is_recording = 1
            led.on()
        elif is_recording == 1 and button.value == True:
            print(''.join(['done', '\n', '\n']))
            recorder.stop()
            led.off()
            is_recording = 0
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    led.close()
    if recorder.status() == 'playing':
        print('recording is running, terminating now!')
        recorder.stop()
    else:
        print('no recording running, exiting now')
