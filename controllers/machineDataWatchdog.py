#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
# import grpc
# import iot_pb2_grpc as iot_pb2_grpc


class MachineWatchdog(Thread):   
    """
    Class to represent a machine watchdog object.
    """

    def __init__(self, machineIP, machinePort, wdTime):
        """
        Initialisation method.
        Parameters:
            machineIP : IP address of the machine.
            machinePort : Port number to kick.
            wdTime : Watchdog time interval.  <TODO>
        """

        Thread.__init__(self)

        # Machine's address and watchdog details.
        self.machineIP = machineIP
        self.machinePort = machinePort
        self.wdTime = wdTime
        self.wdCount = 0

        # Initialise state of the machine watchdog.
        self.stayAlive = True

    def run(self):
        """
        Run threaded method.
        Loop forever, machine kicking watchdog.
        """

        # # Establish the connection to the machine.
        # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        # channel = grpc.insecure_channel(f'{self.machineIP}:{self.machinePort}')
        # stub = iot_pb2_grpc.ControllerMessagesStub(channel)
        # server.start()

        while self.stayAlive:

            self.wdCount += 1

            time.sleep(1)
