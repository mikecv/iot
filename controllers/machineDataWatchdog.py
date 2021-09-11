#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
import grpc
import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc


class MachineWatchdog(Thread):   
    """
    Class to represent a machine watchdog object.
    Kicks machine's watchdog periodically to make sure it is alive.
    """

    def __init__(self, machine, wdTime, wdRetries):
        """
        Initialisation method.
        Parameters:
            machine : Parent MachineData object.
            wdTime : Watchdog time interval.
            wdRetries : Number of retries for watchdog failure.
        """

        Thread.__init__(self)

        # Machine's address and watchdog details.
        self.machine = machine
        self.wdTime = wdTime
        self.wdRetries = wdRetries

        # Watchdog count. If it reaches 0 then retries of watchdog expired.
        self.wdCount = self.wdRetries

        # Initialise state of the machine watchdog.
        self.stayAlive = True

    def run(self):
        """
        Run threaded method.
        Loop forever, controller kicking machine watchdog.
        """

        # Establish the connection to the machine.
        channel = grpc.insecure_channel(f'{self.machine.machineIP}:{self.machine.machinePort}')
        stub = iot_pb2_grpc.ControllerMessagesStub(channel)

        # Construct the watchdog message. Can do here as will be same every time.
        kickCmd = iot_pb2.WatchdogCmd()
        kickCmd.cmd = iot_pb2.ControllerCmd.C_WATCHDOG
        kickCmd.uUID = self.machine.uuid

        while self.stayAlive:

            # Check if watchdog flag has reached retry limit,
            if self.wdCount == 0:
                self.stayAlive = False
                self.machine.dieMachineDie()
            else:
                try:
                    # Try and send a watchdog command to the machine.
                    self.machine.log.debug(f"Kicking watchdog for machine : {self.machine.uuid}; count : {self.wdCount}")

                    # Send a command to kick the machine watchdog.
                    response = stub.KickWatchdog(kickCmd)

                    self.machine.log.debug(f"Watchdog response received, status : {response.status}")
                    if response.status == iot_pb2.ControllerResp.CS_GOOD:
                        self.wdCount = self.wdRetries
                    else:
                        # Watchdog NOT kicked so decrement retry count.
                        self.wdCount -= 1
                except grpc.RpcError as e:
                    # Failed to receive response from machine.
                    self.machine.log.debug(f"GRPC error, status : {e.code()}; details : {e.details()}")
                    # Watchdog error so decrement retry count.
                    self.wdCount -= 1
                    print(f"Missed watchdog count : {self.wdCount}")

            # Wait watchdog period before going around again.
            time.sleep(self.wdTime)
