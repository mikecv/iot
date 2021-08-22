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
            try:
                # Create a new registered machine for the controller.
                newUID = self.ctrl.issueUID()
                clientIP = request.machineIP
                self.ctrl.regNewMachine(newUID, clientIP)

                # Respond to the machine that it is registered.
                return iot_pb2.RegisterResp(status = iot_pb2.MachineStatus.MS_GOOD, uID = newUID)
            except Exception as e:
                # Server-side GRPC error.
                context.set_code(iot_pb2.MachineStatus.MS_SERVER_EXCEPTION)
                context.set_details(f"Server exception : {e}")
                return iot_pb2.iot_pb2.RegisterResp()
        else:
            # Unexpected command in register machine request.
            context.set_code(iot_pb2.MachineStatus.MS_UNEXPECTED_CMD)
            context.set_details("Unexpected command.")
            return iot_pb2.iot_pb2.RegisterResp()
