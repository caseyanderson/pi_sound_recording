#!/usr/bin/python3

'''
wrapper for controlling arecord instances
'''

import subprocess
import os
import signal

class Recorder():

    def __init__(self, path):
        self.path = path
        self.process = None

    def record(self):
        path = self.path
        self.process = subprocess.Popen(['arecord', '-f', 'cd', '-D', 'plughw:1', path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def stop(self):
        self.process.terminate()

    def status(self):
        if self.process.poll() is not None:
            return 'done'
        else:
            return 'playing'

    # def stop(self):
    #     self.process.stdin.write(b'q')
    #     self.process.stdin.flush()



    # def kill(self):
    #     os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
    #
    # def toggle(self):
    #     self.process.stdin.write(b'p')
    #     self.process.stdin.flush()
