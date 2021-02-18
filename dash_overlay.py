import dash_utils as Utils

from dash_camera import CameraService
from dash_gps import GpsService, MODE_NO_FIX
from dash_logger import logging

logger = logging.getLogger("OVERLAY")


class OverlayService:
    def start():
        logger.info("Starting OVERLAY service...")
        OverlayService.interval = Utils.setInterval(1, OverlayService.setOverlay)

    def stop():
        logger.info("Stopping OVERLAY service...")
        OverlayService.interval.cancel()
        logger.info("OVERLAY service stopped successfully.")

    def setOverlay():
        if CameraService.camera.recording:
            CameraService.camera.annotate_text = OverlayService.getOverlay()

    def getOverlay():
        overlay = ""
        overlay += Utils.getOverlaytime() + " - "
        speed = ""

        if GpsService.isValid():
            if GpsService.getData().mode > MODE_NO_FIX:
                speed = str(GpsService.getData().speed()) + " km/h"

            overlay += speed
        else:
            overlay += "no GPS"

        return overlay
