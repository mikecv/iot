#!/usr/bin/env python3

from threading import Thread
import time

from machineDataWatchdog import *

class MachineData(Thread):   
    """
    Class to represent a machine data object.
    This object reflects the information determined for,
    and received from a registered machine.
    """

    def __init__(self, config, log, uid, machineName, machineIP, machinePort):
        """
        Initialisation method.
        Parameters:
            uid : UID of the new machine data object.
            machineIP : IP address of the machine.
            machinePort : Port number to kick.
            wdTime : Watchdog time interval.
        """

        Thread.__init__(self)
        self.cfg = config
        self.log = log

        # Machine's UID and details.
        self.uid = uid
        self.machineName = machineName
        self.machineIP = machineIP
        self.machinePort = machinePort

        # Start a watchdog for the machine.
        self.watchdog = MachineWatchdog(machineIP, machinePort, 1)
        self.watchdog.start()

        # Initialise state of the machine.
        self.stayAlive = True

    def run(self):
        """
        Run threaded method.
        Loop forever and perform processing.
        Mainline will kill thread when self.stayAlive is False.
        """

        while self.stayAlive:

            print(f"Kicking watchdog for UID : {self.uid}; count : {self.watchdog.wdCount}")

            time.sleep(1)
