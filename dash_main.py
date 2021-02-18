from dash_camera import CameraService
from dash_overlay import OverlayService
from dash_disk import DiskService
from dash_gps import GpsService
from dash_logger import logging
from time import sleep

logger = logging.getLogger("MAIN")


def main():
    logger.info("=================================== Starting dash process ===================================")

    CameraService.start()
    OverlayService.start()
    GpsService.start()
    DiskService.start()

    try:
        while True:
            sleep(1)
    except:
        logger.info("=================================== Stopping dash process ===================================")
        CameraService.stop()
        OverlayService.stop()
        GpsService.stop()
        DiskService.stop()


if __name__ == "__main__":
    main()
