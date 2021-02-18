from typing import cast
from dash_system_info import SystemInfo
from dash_logger import logging
from decouple import config
import dash_utils as Utils
import os
from os.path import join, getsize

RECORDINGS_FOLDER = os.path.abspath(config("RECORDINGS_FOLDER"))
MAX_RECORDINGS_SIZE = config("MAX_RECORDINGS_SIZE", cast=int)

logger = logging.getLogger("DISK")


class DiskService:

    recordingsInterval: Utils.setInterval

    def start():
        logger.info("Starting DISK service...")

        DiskService.recordingsInterval = Utils.setInterval(1, DiskService.manageRecordings)

        logger.info("DISK service started successfully.")

    def stop():
        logger.info("Stopping DISK service...")

        DiskService.recordingsInterval.cancel()

        logger.info("DISK service stopped successfully.")

    def manageRecordings():
        if SystemInfo.getUsedSpace(RECORDINGS_FOLDER) > MAX_RECORDINGS_SIZE:
            logger.info(f"[{RECORDINGS_FOLDER}] is over the limit of {Utils.bytesToGigabytes(MAX_RECORDINGS_SIZE)} GB")

            while SystemInfo.getUsedSpace(RECORDINGS_FOLDER) > MAX_RECORDINGS_SIZE:
                try:
                    recordings = os.listdir(RECORDINGS_FOLDER)
                    oldestFile = min([os.path.abspath(RECORDINGS_FOLDER + "/" + f) for f in recordings], key=os.path.getctime)
                    logger.info(f"Deleting [{oldestFile}]")
                    os.remove(oldestFile)
                except Exception as e:
                    logger.error(e)


if __name__ == "__main__":
    print(SystemInfo.getUsedSpace(RECORDINGS_FOLDER))
    print(MAX_RECORDINGS_SIZE)
    DiskService.manageRecordings()