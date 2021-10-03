#!/usr/bin/env python3

import grpc
import iot_pb2 as iot_pb2
import iot_pb2_grpc as iot_pb2_grpc


class ControllerCommands(iot_pb2_grpc.ControllerMessages):
    """
    GRPC ControllerMessages messaging class.
    """

    def __init__(self, machine):
        """
        Initialisation method.
        Parameters:
            machine : Machine object interfaced to.
        """

        self.machine = machine

    def KickWatchdog(self, request, context):
        """
        Respond to watchdog kick from the controller.
        """

        if request.cmd == iot_pb2.ControllerCmd.C_WATCHDOG:
            # Do a check that the machine UID is correct.
            # If not a match then do nothing.
            if request.uUID == self.machine.uUID:
                try:
                    # Reset the last watchdog kicked time.
                    # This is to know that the controller is still there.
                    self.machine.wdKicked()

                    # Respond to the watchdog kick from the controller.
                    # Send the status of the machine.
                    # Send back the same transaction number as in the command message.
                    return iot_pb2.WatchdogResp(tx=request.tx, status=iot_pb2.ControllerResp.CS_GOOD)

                except grpc.RpcError as e:
                    # Client-side GRPC error.
                    context.set_code(iot_pb2.ControllerResp.CS_CLIENT_EXCEPTION)
                    context.set_details(f"Client exception, status : {e.code()}; details : {e.details()}")
                    return iot_pb2.iot_pb2.WatchdogResp()
        else:
            # Unexpected command in watchdog request.
            context.set_code(iot_pb2.ControllerResp.CS_UNEXPECTED_CMD)
            context.set_details("Unexpected command.")
            return iot_pb2.iot_pb2.WatchdogResp()
