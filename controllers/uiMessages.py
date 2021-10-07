#!/usr/bin/env python3


from datetime import datetime
import json
import grpc
import ui_pb2 as ui_pb2
import ui_pb2_grpc as ui_pb2_grpc

class UiCommands(ui_pb2_grpc.UiMessages):
    """
    GRPC UiMessages messaging class.
    """

    def __init__(self, config, controller):
        """
        Initialisation method.
        Parameters:
            config : Mainline configuration object.
            log : Mainline logging object.
        """

        self.cfg = config
        self.ctrl = controller

    def GetControllerStatus(self, request, context):
        """
        Respond to controller status request from controller.
        """

        if request.cmd == ui_pb2.UiCmd.U_CNTRL_STATUS:
            try:
                # Respond to the UI.
                resp = ui_pb2.ControllerStatusResp()
                resp.status = ui_pb2.StatusCmdStatus.US_GOOD
                resp.name = self.cfg.ControllerName
                resp.state = self.ctrl.state.name
                resp.cTime = datetime.now().strftime("%H:%M:%S")
                resp.numMachines = len(self.ctrl.regMachines)
                return resp

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

    def GetMachinesData(self, request, context):
        """
        Respond to machines data request from controller.
        """

        if request.cmd == ui_pb2.UiCmd. U_MACHINE_DATA:
            try:
                # Respond to the UI.
                resp = ui_pb2.MachinesDataResp()
                resp.status = ui_pb2.StatusCmdStatus.US_GOOD
                resp.machinesData = self.MachineDataSerialised()
                return resp

            except grpc.RpcError as e:
                # Server-side GRPC error.
                context.set_code(ui_pb2.StatusCmdStatus.US_SERVER_EXCEPTION)
                context.set_details(f"Server exception, status : {e.code()}; details : {e.details()}")
                return ui_pb2.ui_pb2.MachinesDataResp()
        else:
            # Unexpected command in controller status request.
            context.set_code(ui_pb2.StatusCmdStatus.US_UNEXPECTED_CMD)
            context.set_details("Unexpected command.")
            return ui_pb2.ui_pb2.MachinesDataResp()

    def MachineDataSerialised(self):
        """
        Get machine data and put into a dictionary,
        and then convert to json string.
        Serialising to send to UI if requested.
        """

        mlist = []

        for m in self.ctrl.regMachines:
            mData = {
                "machName" : m.machineName,
                "machSessId" : str(m.sessId),
                "machIp" : m.machineIP,
                "machPort" : m.machinePort
            }
            mlist.append(mData)

        return json.dumps(mlist)