import gpsd
from gpsd import GpsResponse
from dash_logger import logging
import dash_utils as Utils
from subprocess import call
import time

logger = logging.getLogger("GPS")

MODE_ERROR = 0
MODE_NO_FIX = 1
MODE_2DFIX = 2
MODE_3DFIX = 3


class GpsService:

    data = None
    updated = float("-inf")

    def start():
        logger.info("Starting GPS service...")

        GpsService.connect()
        GpsService.interval = Utils.setInterval(1, GpsService.update)

        logger.info("GPS service started successfully.")

    def stop():
        logger.info("Stopping GPS service...")
        GpsService.interval.cancel()
        logger.info("GPS service stopped successfully.")

    def update():

        if GpsService.isConnected():
            try:
                GpsService.data = gpsd.get_current()
                GpsService.updated = time.time()

            except Exception as e:
                logger.error(e)
        else:
            GpsService.connect()

    def connect():
        try:
            call(["sudo /usr/sbin/gpsd /dev/ttyS0 -F /var/run/gpsd.sock"], shell=True)

            while not GpsService.isConnected():
                try:
                    logger.info("GPS attempting connection..")
                    gpsd.connect()
                    time.sleep(1)
                except Exception as e:
                    logger.error(e)

            logger.info("GPS connected.")

        except Exception as e:
            logger.error(e)

    def isValid():
        elapsed = time.time() - GpsService.updated
        return elapsed < 1

    def getData() -> GpsResponse:
        return GpsService.data

    def isConnected():
        try:
            gpsd.device()
            return True
        except:
            return False


if __name__ == "__main__":
    GpsService.start()
    print(gpsd.device())

    print(GpsService.isValid())
    time.sleep(2)

    print(GpsService.getData().speed())