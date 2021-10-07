#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
import grpc
import iot_pb2_grpc as iot_pb2_grpc

from constants import *
from machineCommands import *
from machineData import *


class Controller(Thread):   
    """
    Class to represent a controller.
    Derive from Thread class.
    """

    def __init__(self, config, log):
        """
        Initialisation method.
        Parameters:
            config : Mainline configuration object.
            log : Mainline logging object.
        """

        Thread.__init__(self)
        self.cfg = config
        self.log = log

        # Array of registered machines.
        self.regMachines = []

        # Initialise last session ID issued.
        self.lastSessionId = 0

        # Initialise state of the controller.
        self.stayAlive = True
        self.state = ControllerState.STARTING

    def slotFree(self):
        """
        The controller only has capacity for a limited number of machines (slots).
        If number of slots used then return False so machine not registered.
        """

        self.log.debug(f"Checking for free machine control slot...")
        freeSlot = True
        if len(self.regMachines) == self.cfg.MCtrl["MaxMachines"]:
            self.log.debug(f'Machine control slot allocation full : {self.cfg.MCtrl["MaxMachines"]}')
            freeSlot = False
        return freeSlot

    def getNextSessId(self):
        """
        Assign an Id for the machine.
        Increment the next session I for next time 
        """
        # Increment last session Id.
        self.lastSessionId += 1
        return self.lastSessionId


    def regNewMachine(self, machineName, machineIP, machinePort):
        """
        Register a new machine after allocating a session ID.
        Creates a registered machine data object.
        """

        # Get next session Id for this machine.
        sessId = self.getNextSessId()

        print(f"Registered new machine: \n\tSession ID : {sessId} \n\tName : {machineName} \n\tAddress : {machineIP} \n\tPort : {machinePort}")
        self.log.debug(f"Registered new machine with Session ID : {sessId}; name : {machineName}; address : {machineIP}; port : {machinePort}")

        # Create a machine data object for the machine.
        # Add the machine data object to list of machines.
        md = MachineData(self.cfg, self.log, self, sessId, machineName, machineIP, machinePort)
        self.regMachines.append(md)
        md.start()

        return sessId

    def noMachineSlots(self, machine):
        """
        Failed to register machine because no slots available.
        """

        print(f"Failed to register new machine as no slots available : {machine}")
        self.log.debug(f"Failed to register new machine as no slots available : {machine}")

    def run(self):
        """
        Run threaded method.
        Loop forever, checking for state transitions.
        Mainline will kill thread when self.stayAlive is False.
        """

        # Configure and start the server to listen for messages from machines.
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        iot_pb2_grpc.add_MachineMessagesServicer_to_server(MachineCommands(self), server)
        server.add_insecure_port(f'[::]:{self.cfg.GRPC["ListenPort"]}')
        server.start()

        while self.stayAlive:
            if self.state == ControllerState.STARTING:
                self.log.debug(f"(Re)Starting in state : {self.state}")
                self.state = ControllerState.INITIALISING
            elif self.state == ControllerState.INITIALISING:
                self.log.debug(f"Transition to state : {self.state}")
                self.initialise()
            elif self.state == ControllerState.ACTIVE:
                self.log.debug(f"Transition to state : {self.state}")
                self.controlling()
            elif self.state == ControllerState.TERMINATING:
                self.log.debug(f"Transition to state : {self.state}")
                self.stayAlive = False
            else:
                self.log.error(f"State not supported : {self.state}")

    def initialise(self):
        """
        Initialise class variables and state.
        """

        self.log.debug("Initialising controller...")

        # Initialise stay alive flag.
        self.stayAlive = True

        # Transition to the active state.
        self.state = ControllerState.ACTIVE

    def buryDeadMachine(self, machineData):
        """
        Machine has died, so remove from list of active machines.
        """

        self.log.debug("Removing dead machine from list of active machines...")
        self.regMachines.remove(machineData)

    def controlling(self):
        """
        Performing controlling functions.
        """

        self.log.debug("Performing controller processing...")

        while True:
            for m in self.regMachines:
                pass
                # TODO

            time.sleep(self.cfg.Timers["MainSleep"])
