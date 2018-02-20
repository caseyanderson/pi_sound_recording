#!/usr/bin/python3

from recorder import *

'''
repeatedly trigger a recording for x duration from button press or similar
'''

from recorder import *
from gpiozero import Button

BASE_DIR = '/home/cta/'

NAME =  'a'
DATE = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
FORMAT = '.wav'
FILENAME = ''.join([NAME, DATE, FORMAT])

REC_PATH = ''.join([BASE_DIR, FILENAME])

input_pin = 4
is_recording = 0
duration = 10

button = Button(input_pin)

recorder = Recorder(REC_PATH, duration)

try:
    while True:
        if is_recording == 0 and button.value == True:
            print('button pressed, starting video')
            recorder.record()
            is_playing = 1
        elif is_playing == 1:
            if recorder.status() == 'done':
                print(''.join(['done', '\n', '\n']))
                is_playing = 0
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if recorder.status() == 'playing':
        print('recording is running, terminating now!')
        recorder.stop()
    else:
        print('no recording running, exiting now')
