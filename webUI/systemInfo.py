#!/usr/bin/env python3

from concurrent import futures
from threading import Thread
import time
import grpc
import webUI.ui_pb2 as ui_pb2
import webUI.ui_pb2_grpc as ui_pb2_grpc


class SystemInfo(Thread):   
    """
    Class to get system info from controller.
    Derive from Thread class.
    """

    def __init__(self):
        """
        Initialisation method.
        Parameters:
        """

        Thread.__init__(self)

        # Initialise stale data flag.
        self.staleData = True

        # Set up channel to controller to get status information.
        channel = grpc.insecure_channel('127.0.0.1:50150')
        self.stub = ui_pb2_grpc.UiMessagesStub(channel)

        # Construct command message object.
        self.getStatusCmd = ui_pb2.ControllerStatusCmd()
        self.getStatusCmd.cmd = ui_pb2.UiCmd.U_CNTRL_STATUS

    def run(self):
        """
        Run threaded method.
        Loop forever, getting system info from controller.
        """
        while True:
            try:
                # Send status request command to the server.
                response = self.stub.GetControllerStatus(self.getStatusCmd)

                if response.status == ui_pb2.StatusCmdStatus.US_GOOD:
                    # Status response good, so update status object.
                    self.staleData = True
                else:
                    self.staleData = False
            except grpc.RpcError as e:
                # Failed to receive response from server.
                print(f"GRPC error, status : {e.code()}; details : {e.details()}")
        
            # Sleep and then get updated data.
            time.sleep(1.0)
