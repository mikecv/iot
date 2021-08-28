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

    def __init__(self, config, log, uuid, machineName, machineIP, machinePort):
        """
        Initialisation method.
        Parameters:
            uuid : UUID of the new machine data object.
            machineIP : IP address of the machine.
            machinePort : Port number to kick.
            wdTime : Watchdog time interval.
        """

        Thread.__init__(self)
        self.cfg = config
        self.log = log

        # Machine's UID and details.
        self.uuid = uuid
        self.machineName = machineName
        self.machineIP = machineIP
        self.machinePort = machinePort

        # Start a watchdog for the machine.
        self.watchdog = MachineWatchdog(self, 1)
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

            time.sleep(1)

    def dieMachineDie(self):
        """
        Machine needs to be killed off.
        This is most likely due to the machine not being responsive.
        """

        print(f"Killing off machine, UUID : {self.uuid}")
        self.stayAlive = False