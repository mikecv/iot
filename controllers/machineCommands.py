#!/usr/bin/env python3

import grpc
import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc


class MachineCommands(iot_pb2_grpc.MachineMessages):
    """
    GRPC MachineMessages messaging class.
    """

    def __init__(self, ctrl) -> None:
        """
        Initialisation method.
        Parameters:
            controller : Controller object listening.
        """

        self.ctrl = ctrl

    def RegisterMachine(self, request, context) -> iot_pb2.RegisterResp:
        """
        Respond to register machine request from machine.
        Parameters:
            request : gRPC request message details.
            context : gRPC message context.
        """

        if request.cmd == iot_pb2.MachineCmd.M_REGISTER:
            try:
                clientName = request.machineName
                if self.ctrl.slotFree():
                    # Create a new registered machine for the controller.
                    clientIP = request.machineIP
                    clientPort = request.machinePort
                    sId = self.ctrl.regNewMachine(clientName, clientIP, clientPort)

                    # Respond to the machine that it is registered.
                    return iot_pb2.RegisterResp(status = iot_pb2.MachineStatus.MS_GOOD, sessId = sId)
                else:
                    # Advise controller that registration failed as no slots available.
                    self.ctrl.noMachineSlots(clientName)

                    # Respond to the machine that registration failed as no slots are free.
                    return iot_pb2.RegisterResp(status = iot_pb2.MachineStatus.MS_NO_SLOT, sId = 0)

            except grpc.RpcError as e:
                # Server-side GRPC error.
                context.set_code(iot_pb2.MachineStatus.MS_SERVER_EXCEPTION)
                context.set_details(f"Server exception, status : {e.code()}; details : {e.details()}")
                return iot_pb2.iot_pb2.RegisterResp()
        else:
            # Unexpected command in register machine request.
            context.set_code(iot_pb2.MachineStatus.MS_UNEXPECTED_CMD)
            context.set_details("Unexpected command.")
            return iot_pb2.iot_pb2.RegisterResp()
