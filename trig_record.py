#!/usr/bin/python3

'''
repeatedly trigger a recording for x duration from button press or similar
'''

from recorder import *
from gpiozero import Button
from gpiozero import LED
from datetime import datetime

BASE_DIR = '/home/cta/'

NAME =  ''
FORMAT = '.wav'

input_pin = 4
led_pin = 17
is_recording = 0
duration = 15

button = Button(input_pin)
led = LED(led_pin)

print("ready to record!")

try:
    while True:
        if is_recording == 0 and button.value == True:

            print('button pressed, setting up and starting recording')
            DATE = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
            REC_PATH = ''.join([BASE_DIR, NAME, DATE, FORMAT])
            recorder = Recorder(REC_PATH, duration)
            recorder.record()
            led.on()
            is_recording = 1
        elif is_recording == 1:
            if recorder.status() == 'done':
                print(''.join(['done', '\n', '\n']))
                led.off()
                is_recording = 0
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if recorder.status() == 'playing':
        print('recording is running, terminating now!')
        recorder.stop()
    else:
        print('no recording running, exiting now')
