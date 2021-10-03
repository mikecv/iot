from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
import json
import grpc
import webUI.ui_pb2 as ui_pb2
import webUI.ui_pb2_grpc as ui_pb2_grpc

from flask import current_app
from webUI.auth import login_required
from webUI.db import get_db

bp = Blueprint('webUI', __name__)

@bp.route('/')
def index():
    """
    Index (start) page for webUI.
    """

    # Set up channel to controller to get status information.
    channel = grpc.insecure_channel(f'{current_app.config["UI_IP"]}:{current_app.config["UI_PORT"]}')
    stub = ui_pb2_grpc.UiMessagesStub(channel)

    # Construct controller status request message object.
    getStatusCmd = ui_pb2.ControllerStatusCmd()
    getStatusCmd.cmd = ui_pb2.UiCmd.U_CNTRL_STATUS

    # Initialise flag for stale data,
    # i.e. if no or failed status response from controller.
    staleData = True
    cntrlData = {}
    machData = []

    # Initialise web page refresh rate to slow.
    # If connected to a controller then can speed up.
    updatePeriod = current_app.config["UI_REFRESH_PERIOD_SLOW"]
    try:
        # Send status request command to the server.
        response = stub.GetControllerStatus(getStatusCmd)

        if response.status == ui_pb2.StatusCmdStatus.US_GOOD:
            # Status response good, so update controller status object.
            staleData = False
            cntrlData = {
                "name" : response.name,
                "state" : response.state,
                "cTime" : response.cTime,
                "nMach" : response.numMachines
            }

            # If we have a response from controller, and there are some connedted machines,
            # Send another request to get machines data.
            if cntrlData["nMach"] > 0:
                # Construct controller status request message object.
                getDataCmd = ui_pb2.MachinesDataCmd()
                getDataCmd.cmd = ui_pb2.UiCmd.U_MACHINE_DATA

                try:
                    # Send status request command to the server.
                    response2 = stub.GetMachinesData(getDataCmd)

                    if response2.status == ui_pb2.StatusCmdStatus.US_GOOD:
                        # Data response good, so update machine data object.
                        # Need to deserialise json data back to list of data for machines.
                        machData = json.loads(response2.machinesData)

                except grpc.RpcError as e:
                    # Failed to receive response from server.
                    pass

            # Speed up web page refresh rate now that we are connected.
            updatePeriod = current_app.config["UI_REFRESH_PERIOD_FAST"]

    except grpc.RpcError as e:
        # Failed to receive response from server.
        pass

    return render_template('webUI/index.html', refresh=updatePeriod, linkStale=staleData, cData=cntrlData, mData=machData)
