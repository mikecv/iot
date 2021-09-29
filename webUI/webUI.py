from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
import time
import grpc
import webUI.ui_pb2 as ui_pb2
import webUI.ui_pb2_grpc as ui_pb2_grpc

from webUI.auth import login_required
from webUI.db import get_db
from webUI.systemInfo import SystemInfo

bp = Blueprint('webUI', __name__)

@bp.route('/')
def index():
    """
    Index (start) page for webUI.
    """

    # Set up channel to controller to get status information.
    channel = grpc.insecure_channel('127.0.0.1:50150')
    stub = ui_pb2_grpc.UiMessagesStub(channel)

    # Construct command message object.
    getStatusCmd = ui_pb2.ControllerStatusCmd()
    getStatusCmd.cmd = ui_pb2.UiCmd.U_CNTRL_STATUS

    # Initialise flag for stale data,
    # i.e. if no or failed status response from controller.
    staleData = True
    try:
        # Send status request command to the server.
        response = stub.GetControllerStatus(getStatusCmd)

        if response.status == ui_pb2.StatusCmdStatus.US_GOOD:
            # Status response good, so update status object.
            # <TODO> deserialise data and pass to template.
            staleData = False
    except grpc.RpcError as e:
        # Failed to receive response from server.
        print("GRPC error getting controller status.")

    return render_template('webUI/index.html', link=staleData)
