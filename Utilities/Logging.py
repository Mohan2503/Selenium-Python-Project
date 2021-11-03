import logging


class Logger:
    logging.basicConfig(filename="..\\logs\\project.log", filemode="w")
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
