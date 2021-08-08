#!/usr/bin/env python3

from threading import Thread
import grpc
import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc

from constants import *


class Machine(Thread):   
    """
    Class to represent a machine.
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

        # Initialise state of the machine.
        self.stayAlive = True
        self.state = MachineState.STARTING

    def run(self):
        """
        Run threaded method.
        Loop forever, checking for state transitions.
        Mainline will kill thread when self.stayAlive is False.
        """

        while self.stayAlive:
            if self.state == MachineState.STARTING:
                self.log.debug(f"(Re)Starting in state : {self.state}")
                self.state = MachineState.INITIALISING
            elif self.state == MachineState.INITIALISING:
                self.log.debug(f"Transition to state : {self.state}")
                self.initialise()
            elif self.state == MachineState.REGISTERING:
                self.log.debug(f"Transition to state : {self.state}")
                self.register()
            elif self.state == MachineState.TERMINATING:
                self.log.debug(f"Transition to state : {self.state}")
                self.stayAlive = False
            elif self.state == MachineState.ACTIVE:
                self.log.debug(f"Transition to state : {self.state}")
                self.process()
            else:
                self.log.error(f"State not supported : {self.state}")

    def initialise(self):
        """
        Initialise class variables and state.
        """

        self.log.info("Initialising machine.")

        # Initialise stay alive flag.
        self.stayAlive = True

        # Transition to the Registering state.
        self.state = MachineState.REGISTERING

    def register(self):
        """
        Register the machine with the controller.
        """

        self.log.info("Registering machine with controller.")

        channel = grpc.insecure_channel(f'{self.cfg.GRPC["ServerIP"]}:{self.cfg.GRPC["ServerPort"]}')
        stub = iot_pb2_grpc.MachineMessagesStub(channel)
        try:
            # Try and send a register machine command to the server.
            response = stub.RegisterMachine(iot_pb2.RegisterCmd(cmd=iot_pb2.MachineCmd.M_REGISTER))
            self.log.debug(f"Registration response received, status : {response.status}; uID : {response.uID}")
            print(f"Registration response received, status : {response.status}; uID : {response.uID}")
            self.state = MachineState.ACTIVE
        except grpc.RpcError as rpc_error:
            # Failed to receive response from server.
            self.log.debug(f"GRPC error, code : {rpc_error.code()}; message : {rpc_error.details()}")
            print(f"GRPC error, code : {rpc_error.code()}; message : {rpc_error.details()}")
            self.state = MachineState.TERMINATING

    def process(self):
        """
        Controller is active and registered, so process.
        """

        self.log.info("Machine registered and processing.")
        while True:
            pass
