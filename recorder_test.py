#!/usr/bin/python3

'''
wrapper for controlling arecord instances
'''

import subprocess
import os
import signal

class Recorder():

    def __init__(self, path, dur): # duration of 0 results in an "infinite" recording
        self.dur = dur
        self.path = path
        self.process = None

    def record(self):
        path = self.path
        dur = self.dur
        self.process = subprocess.Popen(['arecord', '-f', 'cd', '-D', 'plughw:1', '-d', str(dur), str(path)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def record_monitor(self):
        path = self.path
        dur = self.dur
        # self.process = subprocess.Popen(['arecord', '-f', 'cd', '-D', 'plughw:1', '-d', str(dur), str(path)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        self.process = subprocess.Popen(['arecord', '-f', 'cd', '-D', 'plughw:1', '-d', str(dur), str(path), '|', 'aplay', '-D', 'plughw:CARD=1', 'DEV=0' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def status(self):
        if self.process.poll() is not None:
            return 'done'
        else:
            return 'playing'

    def stop(self):
        self.process.terminate()
        self.process.kill()
