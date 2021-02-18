import logging
from decouple import config

LOG_FOLDER = config('LOG_FOLDER')


class Logger:

    logging.basicConfig(
        format='%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s',
        # filename=LOG_FOLDER + "dash.log",
        level=logging.INFO)
