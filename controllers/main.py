#!/usr/bin/env python3

import argparse
import logging
import logging.handlers
import time

from config import *
from controller import *

# *******************************************
# Program history.
# 0.1   MDC 23/07/2021  Original.
# *******************************************

# *******************************************
# TODO List
#
# *******************************************

# Program name, version, and date.
progName = "controller"
progVersion = "0.1"
progDate = "2021"

# Program main.
def main(cFile, lFile):
    """
    Controller mainline.
    Parameters:
        cFile : Json configuration file.
        lFile : Program log file.
    """

    # Create configuration values class object.
    cfg = Config(cFile)

    # Create logger. Use rotating log files.
    logger = logging.getLogger(progName)
    logger.setLevel(cfg.DebugLevel)
    handler = logging.handlers.RotatingFileHandler(lFile, maxBytes=cfg.LogFileSize, backupCount=cfg.LogBackups)
    handler.setFormatter(logging.Formatter(fmt="%(asctime)s.%(msecs)03d [%(name)s] [%(levelname)-8s] %(message)s", datefmt="%Y%m%d-%H:%M:%S", style="%"))
    logging.Formatter.converter = time.localtime
    logger.addHandler(handler)

    # Log program version.
    logger.info(f"Program version : {progVersion}")

    # Create an instance of a controller.
    # Controller is a threaded class so start the thread running.
    c = Controller(cfg, logger)
    c.start()

    # Keep checking if controller is still alive,
    # if so, keep processing.
    while c.stayAlive:
        pass

    # Controller not alive, so exit.
    logger.info("Controller is dead.")
    exit(0)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="IoT Controller.")
    parser.add_argument("-c", "--config", help="Json configuration file.")
    parser.add_argument("-l", "--log", help="Log file.")
    parser.add_argument("-v", "--version", help="Program version.", action="store_true")
    args = parser.parse_args()

    # Check if program version requested.
    # Only show version and don't do anything else.
    if args.version:
        print(f"Program version : {progVersion}")
    else:
        # Check that a configuration file specified, else nothing to do.
        # Use default config & log file names if not specified.
        cFile = progName + ".json"
        lFile = progName + ".log"
        if args.config:
            cFile = args.config
        if args.log:
            lFile = args.log
        main(cFile, lFile)
