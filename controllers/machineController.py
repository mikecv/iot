#!/usr/bin/env python3

import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc


class MachineController(iot_pb2_grpc.MachineMessages):
    """
    GRPC MachineMessages messaging class.
    """

    def __init__(self, controller):
        self.ctrl = controller

    def RegisterMachine(self, request, context):
        if request.cmd == iot_pb2.MachineCmd.M_REGISTER:
            # Create a new registered machine for the controller.
            newUID = self.ctrl.issueUID()
            clientIP = request.machineIP
            self.ctrl.regNewMachine(newUID, clientIP)

            # Respond to the machine that it is registered.
            resp = iot_pb2.RegisterResp()
            resp.status = iot_pb2.MachineStatus.MS_GOOD
            resp.uID = newUID

            return resp
