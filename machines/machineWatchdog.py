#!/usr/bin/env python3

import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc


class MachineWatchdog(iot_pb2_grpc.ControllerMessages):
    """
    GRPC ControllerMessages messaging class.
    """

    def __init__(self, controller):
        self.ctrl = controller

    def KickWatchdog(self, request, context):
        if request.cmd == iot_pb2.ControllerCmd.C_WATCHDOG:

            # Respond to the watchdog kick from the controller.
            return iot_pb2.WatchdogResp(status=iot_pb2.ControllerResp.CS_GOOD)
