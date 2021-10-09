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

    def __init__(self, config, log, controller, sessId, machineName, machineIP, machinePort) -> None:
        """
        Initialisation method.
        Parameters:
            config : The controller configuration.
            log : The controller's loggger.
            controller : The controller the machines answer to.
            sessId : Session ID of the new machine data object.
            machineIP : IP address of the machine.
            machinePort : Port number to kick.
        """

        Thread.__init__(self)
        self.cfg = config
        self.log = log

        # Machine's UID and details.
        self.controller = controller
        self.sessId = sessId
        self.machineName = machineName
        self.machineIP = machineIP
        self.machinePort = machinePort

        # Transaction number.
        self.tx = 0

        # Start a watchdog for the machine.
        self.watchdog = MachineWatchdog(self, self.cfg.Timers["WatchDog"], self.cfg.MCtrl["WatchdogRetries"])
        self.watchdog.start()

        # Initialise state of the machine.
        self.stayAlive = True

    def run(self) -> None:
        """
        Run threaded method.
        Loop forever and perform processing.
        Mainline will kill thread when self.stayAlive is False.
        """

        while self.stayAlive:

            time.sleep(self.cfg.MCtrl["LoopTime"])

    def dieMachineDie(self) -> None:
        """
        Machine needs to be killed off.
        This is most likely due to the machine not being responsive.
        """

        print(f"Killing off machine, Session Id : {self.sessId}")
        self.log.debug(f"Killing off machine,  Session Id : {self.sessId}")
        self.stayAlive = False
        self.controller.buryDeadMachine(self)

    def getNextTxNumber(self) -> int:
        """
        Return the next transaction number to be used for messages to the machine.
        Increment the transaction number for next message.
        Returns:
            Transaction number to use in message.
        """

        # Get current transaction number, and increment for next time.
        thisTx = self.tx
        self.tx += 1

        return thisTx
