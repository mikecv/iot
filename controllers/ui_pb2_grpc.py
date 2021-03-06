# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ui_pb2 as ui__pb2


class UiMessagesStub(object):
    """*****************************************
    User Interface message service
    *****************************************
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetControllerStatus = channel.unary_unary(
                '/ui.UiMessages/GetControllerStatus',
                request_serializer=ui__pb2.ControllerStatusCmd.SerializeToString,
                response_deserializer=ui__pb2.ControllerStatusResp.FromString,
                )
        self.GetMachinesData = channel.unary_unary(
                '/ui.UiMessages/GetMachinesData',
                request_serializer=ui__pb2.MachinesDataCmd.SerializeToString,
                response_deserializer=ui__pb2.MachinesDataResp.FromString,
                )


class UiMessagesServicer(object):
    """*****************************************
    User Interface message service
    *****************************************
    """

    def GetControllerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMachinesData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UiMessagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetControllerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControllerStatus,
                    request_deserializer=ui__pb2.ControllerStatusCmd.FromString,
                    response_serializer=ui__pb2.ControllerStatusResp.SerializeToString,
            ),
            'GetMachinesData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMachinesData,
                    request_deserializer=ui__pb2.MachinesDataCmd.FromString,
                    response_serializer=ui__pb2.MachinesDataResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ui.UiMessages', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UiMessages(object):
    """*****************************************
    User Interface message service
    *****************************************
    """

    @staticmethod
    def GetControllerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ui.UiMessages/GetControllerStatus',
            ui__pb2.ControllerStatusCmd.SerializeToString,
            ui__pb2.ControllerStatusResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMachinesData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ui.UiMessages/GetMachinesData',
            ui__pb2.MachinesDataCmd.SerializeToString,
            ui__pb2.MachinesDataResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
