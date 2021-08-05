#!/usr/bin/env python3

import iot_pb2 as pb2
import iot_pb2_grpc as pb2_grpc


class MachineController(pb2_grpc.MachineControl):
    """
    GRPC MachineControl messaging class.
    """

    def __init__(self, controller):
        self.ctrl = controller

    def RegisterMachine(self, request, context):
        if request.cmd == 1:
            # Create a new registered machine for the controller.
            newUID = self.ctrl.issueUID()
            self.ctrl.regNewMachine(newUID)

            # Respond to the machine that it is registered.
            return pb2.RegisterResp(status=0, uID=newUID)
