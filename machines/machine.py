#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
import grpc
import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc

from constants import *
from controllerCommands import *


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
        self.lastKickTime = 0
        self.registerd = False
        self.stayAlive = True
        self.state = MachineState.STARTING

        # Initialise machine variables.
        self.sessId = 0

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


    def wdKicked(self):
        """
        Watchdog kicked by controller so reset the kick time.
        Used to check that controller is still kicking (controlling)
        the machine
        """

        self.lastKickTime = time.time()

    def initialise(self):
        """
        Initialise class variables and state.
        """

        self.log.debug("Initialising machine...")

        # Initialise stay alive flag.
        self.stayAlive = True

        # Initialise machine session Id.
        self.sessId = 0

        # Transition to the Registering state.
        self.registered = False
        self.state = MachineState.REGISTERING

    def register(self):
        """
        Register the machine with the controller.
        """

        self.log.debug("Registering machine with controller...")

        # Set up channel to controller to register the machine.
        channel = grpc.insecure_channel(f'{self.cfg.GRPC["ServerIP"]}:{self.cfg.GRPC["ServerPort"]}')
        stub = iot_pb2_grpc.MachineMessagesStub(channel)

        # Construct command message object.
        regCmd = iot_pb2.RegisterCmd()
        regCmd.cmd = iot_pb2.MachineCmd.M_REGISTER
        regCmd.machineName = self.cfg.MachineName
        regCmd.machineIP = self.cfg.IPaddress
        regCmd.machinePort = self.cfg.IPport

        regTries = 0
        for regTries in range(0, self.cfg.Machine["RegRetries"]):
            try:
                # Try and send a register machine command to the server.
                self.log.debug(f"Attempting to register machine with controller attempt : {regTries+1}")
                print(f"Registering with controller, attempt : {regTries+1}")

                # Send registration command to the server.
                response = stub.RegisterMachine(regCmd)

                self.log.debug(f"Registration response received, status : {response.status}; Session Id : {response.sessId}")
                print(f"Registration response received: \n\tStatus : {response.status} \n\tSession Id : {response.sessId}")
                if response.status == iot_pb2.MachineStatus.MS_GOOD:
                    # Registration response good, so go to active state.
                    self.state = MachineState.ACTIVE
                    self.sessId = response.sessId
                    self.lastKickTime = time.time()
                    self.registered = True
                elif response.status == iot_pb2.MachineStatus.MS_NO_SLOT:
                    # Registration failed because no slots remaining with controller.
                    self.sessId = 0
                    self.registered = False
                else:
                    regTries += 1
            except grpc.RpcError as e:
                # Failed to receive response from server.
                self.log.debug(f"GRPC error, status : {e.code()}; details : {e.details()}")

            # Didn't register then wait a bit and then go back and retry registration, else break.
            if (self.registered == False) and (regTries < (self.cfg.Machine["RegRetries"]-1)):
                time.sleep(self.cfg.Machine["RegDelay"])
            else:
                break

        # If machine was not registered after configurable retries then terminate.
        if self.registered == False:
            self.state = MachineState.TERMINATING

    def process(self):
        """
        Machine is active and registered, so process.
        """

        # Processing so start listening to the controller.
        # Configure and start the server to listen for messages from the controller.
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        iot_pb2_grpc.add_ControllerMessagesServicer_to_server(ControllerCommands(self), server)
        server.add_insecure_port(f'[::]:{self.cfg.IPport}')
        server.start()

        print("Machine registered and processing...")
        while self.registered:

            # Check if still being kicked by the controller.
            # If not then need to die as need a controller.
            curTime = time.time()
            if (curTime - self.lastKickTime) > self.cfg.Machine["ControlAwayTime"]:
                self.log.debug("Controller watchdog kick not received.")
                print("Controller watchdog kick not received.")

                # Initialise the machine again.
                # This will cause the machine to register with the controller again.
                self.registered = False
                self.initialise()
