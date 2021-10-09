#!/usr/bin/env python3

import argparse
import logging
import logging.handlers

from config import *
from machine import *

# *******************************************
# Program history.
# 0.1   MDC 23/07/2021  Original.
# *******************************************

# *******************************************
# TODO List
#
# *******************************************

# Program name, version, and date.
progName = "machine"
progVersion = "0.1"
progDate = "2021"

# Program main.
def main(cFile: str, lFile: str) -> None:
    """
    Machine mainline.
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
    handler.setFormatter(logging.Formatter(fmt=f"%(asctime)s.%(msecs)03d [{cfg.MachineName}] [%(levelname)-8s] %(message)s", datefmt="%Y%m%d-%H:%M:%S", style="%"))
    logging.Formatter.converter = time.localtime
    logger.addHandler(handler)

    # Log program version.
    logger.info(f"Program version : {progVersion}")

    # Create an instance of a machine.
    # Machine is a threaded class so start the thread running.
    m = Machine(cfg, logger)
    m.start()

    # Keep checking if machine is still alive,
    # if so, keep processing.
    while m.stayAlive:
        pass

    # Machine not alive, so exit.
    logger.info("Machine is dead.")
    exit(0)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="IoT Machine.")
    parser.add_argument("-c", "--config", help="Json configuration file.")
    parser.add_argument("-l", "--log", help="Log file.")
    parser.add_argument("-v", "--version", help="Program version.", action="store_true")
    args = parser.parse_args()

    # Check if program version requested.
    # Only show version and don't do anything else.
    if args.version:
        print(f"Program version : {progVersion}")
    else:
        # Use default config & log file names if not specified.
        cFile = progName + ".json"
        lFile = progName + ".log"
        if args.config:
            cFile = args.config
        if args.log:
            lFile = args.log
        main(cFile, lFile)
