#!/usr/bin/env python3

import grpc
import ui_pb2 as ui_pb2
import ui_pb2_grpc as ui_pb2_grpc

class UiCommands(ui_pb2_grpc.UiMessages):
    """
    GRPC UiMessages messaging class.
    """

    def __init__(self, config, controller):
        self.cfg = config
        self.ctrl = controller

    def GetControllerStatus(self, request, context):
        if request.cmd == ui_pb2.UiCmd.U_CNTRL_STATUS:
            try:
                # Respond to the UI.
                # return ui_pb2.ControllerStatusResp(status = ui_pb2.StatusCmdStatus.US_GOOD, name = self.cfg.ControllerName, state = self.ctrl.state)
                return ui_pb2.ControllerStatusResp(status = ui_pb2.StatusCmdStatus.US_GOOD, name = self.cfg.ControllerName, state = str(self.ctrl.state))

            except grpc.RpcError as e:
                # Server-side GRPC error.
                context.set_code(ui_pb2.StatusCmdStatus.US_SERVER_EXCEPTION)
                context.set_details(f"Server exception, status : {e.code()}; details : {e.details()}")
                return ui_pb2.ui_pb2.ControllerStatusResp()
        else:
            # Unexpected command in controller status request.
            context.set_code(ui_pb2.StatusCmdStatus.US_UNEXPECTED_CMD)
            context.set_details("Unexpected command.")
            return ui_pb2.ui_pb2.ControllerStatusResp()
