from typing import cast
import dash_utils as Utils
from dash_logger import logging
from time import sleep
from picamera import PiCamera
from decouple import config


OUTPUT_FOLDER = config("OUTPUT_FOLDER")
RECORDINGS_FOLDER = config("RECORDINGS_FOLDER")
RECORDING_INTERVAL = config("RECORDING_INTERVAL", cast=int)
CAMERA_RESOLUTION = config("CAMERA_RESOLUTION")
CAMERA_FRAMERATE = config("CAMERA_FRAMERATE", cast=int)

logger = logging.getLogger("CAMERA")


class CameraService:
    camera = PiCamera()
    camera.resolution = CAMERA_RESOLUTION
    camera.framerate = CAMERA_FRAMERATE

    def snapshot():
        logger.info("Taking snapshot..")

        targetFile = OUTPUT_FOLDER + "/snapshot/" + Utils.getTimeForFileName() + "_snapshot.jpg"

        CameraService.camera.capture(targetFile)
        logger.info("Snapshot saved to [" + targetFile + "]")

        return targetFile

    def recordNewFile():
        targetFile = RECORDINGS_FOLDER + "/" + Utils.getTimeForFileName() + ".h264"

        if CameraService.camera.recording:
            logger.info("Switching recording to [" + targetFile + "]")
            CameraService.camera.split_recording(targetFile)
        else:
            logger.info("Starting recording to [" + targetFile + "]")
            CameraService.camera.start_recording(targetFile)

    def start():
        logger.info("Starting continuous recording...")
        logger.info("Revision: " + str(CameraService.camera.revision))
        logger.info("Resolution: " + str(CameraService.camera.resolution))
        logger.info("Framerate: " + str(CameraService.camera.framerate))
        logger.info("Recording interval: " + str(RECORDING_INTERVAL))

        CameraService.recordNewFile()
        CameraService.interval = Utils.setInterval(RECORDING_INTERVAL, CameraService.recordNewFile)

    def stop():
        logger.info("Stopping continuous recording...")
        CameraService.interval.cancel()
        CameraService.camera.stop_recording()


if __name__ == "__main__":
    pass