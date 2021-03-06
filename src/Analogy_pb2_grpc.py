# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Analogy_pb2 as Analogy__pb2


class AnalogyStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeForSendMessages = channel.stream_unary(
                '/greet.Analogy/SubscribeForSendMessages',
                request_serializer=Analogy__pb2.AnalogyLogMessage.SerializeToString,
                response_deserializer=Analogy__pb2.AnalogyMessageReply.FromString,
                )
        self.SubscribeForConsumeMessages = channel.unary_stream(
                '/greet.Analogy/SubscribeForConsumeMessages',
                request_serializer=Analogy__pb2.AnalogyConsumerMessage.SerializeToString,
                response_deserializer=Analogy__pb2.AnalogyLogMessage.FromString,
                )


class AnalogyServicer(object):
    """The greeting service definition.
    """

    def SubscribeForSendMessages(self, request_iterator, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeForConsumeMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalogyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeForSendMessages': grpc.stream_unary_rpc_method_handler(
                    servicer.SubscribeForSendMessages,
                    request_deserializer=Analogy__pb2.AnalogyLogMessage.FromString,
                    response_serializer=Analogy__pb2.AnalogyMessageReply.SerializeToString,
            ),
            'SubscribeForConsumeMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeForConsumeMessages,
                    request_deserializer=Analogy__pb2.AnalogyConsumerMessage.FromString,
                    response_serializer=Analogy__pb2.AnalogyLogMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Analogy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Analogy(object):
    """The greeting service definition.
    """

    @staticmethod
    def SubscribeForSendMessages(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/greet.Analogy/SubscribeForSendMessages',
            Analogy__pb2.AnalogyLogMessage.SerializeToString,
            Analogy__pb2.AnalogyMessageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeForConsumeMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.Analogy/SubscribeForConsumeMessages',
            Analogy__pb2.AnalogyConsumerMessage.SerializeToString,
            Analogy__pb2.AnalogyLogMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
