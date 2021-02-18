import time
import threading
from datetime import datetime


class setInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime - time.time()):
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()


def getTimeForFileName():
    return datetime.today().strftime("%Y-%m-%d_%H-%M-%S")


def getOverlaytime():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def bytesToKiloBytes(bytes):
    return round(bytes / 1024, 2)


def bytesToMegabytes(bytes):
    return round(bytesToKiloBytes(bytes) / 1024, 2)


def bytesToGigabytes(bytes):
    return round(bytesToMegabytes(bytes) / 1024, 2)
