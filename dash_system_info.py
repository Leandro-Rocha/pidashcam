from gpiozero import CPUTemperature
import os
import shutil
import time
import uptime


class SystemInfo:
    cpuTemp = CPUTemperature()

    def getTemp():
        return str(SystemInfo.cpuTemp.temperature)

    def getFreeSpace(path="/"):
        return str(round(shutil.disk_usage(path).free, 1))

    def getUsedSpace(path="/"):
        fullFileList = [os.path.abspath(path) + "/" + f for f in os.listdir(path)]
        return sum(os.path.getsize(f) for f in fullFileList if os.path.isfile(f))

    def getUptime():
        return str(time.strftime("%H:%M:%S", time.gmtime(uptime.uptime())))


if __name__ == "__main__":
    print("getTemp: " + SystemInfo.getTemp())
    print("getFreeSpace: " + SystemInfo.getFreeSpace())
    print("getUptime: " + SystemInfo.getUptime())
    # print("getUsedSpace: " + str(SystemInfo.getUsedSpace()))
    print("getUsedSpace: " + str(SystemInfo.getUsedSpace("./output/recordings/")))
