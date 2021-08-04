#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import grpc
import iot_pb2_grpc as pb2_grpc

from constants import *
from machineController import *


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

        # Initialise state of the controller.
        self.stayAlive = True
        self.state = ControllerState.STARTING

    def run(self):
        """
        Run threaded method.
        Loop forever, checking for state transitions.
        Mainline will kill thread when self.stayAlive is False.
        """

        # Configure and start the server to listen for messages from machines.
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_MachineControlServicer_to_server(MachineController(self.cfg, self.log), server)
        server.add_insecure_port('[::]:50051')
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

        self.log.info("Initialising controller.")

        # Initialise stay alive flag.
        self.stayAlive = True

        # Transition to the active state.
        self.state = ControllerState.ACTIVE


    def controlling(self):
        """
        Performing controlling functions.
        """

        self.log.info("Performaing controller processing.")

        while True:
            pass
