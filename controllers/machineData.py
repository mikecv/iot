#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
import grpc
import iot_pb2_grpc as iot_pb2_grpc


class MachineData(Thread):   
    """
    Class to represent a a machine data object.
    This object reflects the information determined for,
    and received from a registered machine.
    """

    def __init__(self, config, log, uid, machineIP):
        """
        Initialisation method.
        Parameters:
            uid : UID of the new machine data object.
        """

        Thread.__init__(self)
        self.cfg = config
        self.log = log

        # Machine's UID.
        self.uid = uid
        self.ipmachineIP = machineIP

        # Initialise state of the machine.
        self.stayAlive = True

    def run(self):
        """
        Run threaded method.
        Loop forever, check if machine still alive by kicking watchdog, and perform processing.
        Mainline will kill thread when self.stayAlive is False.
        """

        # Establish theconnection to the machine.
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        channel = grpc.insecure_channel(f'{self.machineIP}:{self.cfg.GRPC["ServerPort"]}')
        stub = iot_pb2_grpc.ControllerMessagesStub(channel)
        server.start()

        while self.stayAlive:
            print("Processing machine...")
            pass

            # TODO

            time.sleep(self.cfg.MCtrl["LoopTime"])
