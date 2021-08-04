#!/usr/bin/env python3

import iot_pb2 as pb2
import iot_pb2_grpc as pb2_grpc


class MachineController(pb2_grpc.MachineControl):
    """
    GRPC MachineControl messaging class.
    """

    def __init__(self, config, log):
        self.cfg = config
        self.log = log

    def RegisterMachine(self, request, context):
        if request.cmd == 1:
            self.log.debug(f"Registration command received, cmd : {request.cmd}")
            print(f"Registration command received, cmd : {request.cmd}")
            return pb2.RegisterResp(status=0, uID=1)
