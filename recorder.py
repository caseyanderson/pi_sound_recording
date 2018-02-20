#!/usr/bin/python3

'''
wrapper for controlling arecord instances
'''

import subprocess
import os
import signal

class Recorder():

    def __init__(self, path, dur):
        self.dur = dur
        self.path = path
        self.process = None

    def record(self):
        path = self.path
        dur = self.dur
        self.process = subprocess.Popen(['arecord', '-f', 'cd', '-D', 'plughw:1', '-d', str(dur), str(path)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def status(self):
        if self.process.poll() is not None:
            return 'done'
        else:
            return 'playing'

    def stop(self):
        self.process.terminate()
        self.process.kill()
