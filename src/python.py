import grpc
import Analogy_pb2
import Analogy_pb2_grpc


def make_message(message):
    return Analogy_pb2.AnalogyLogMessage(
        Text=message,
	Level="Information"
    )


def generate_messages():
    messages = [
        make_message("First message"),
        make_message("Second message"),
        make_message("Third message"),
        make_message("Fourth message"),
        make_message("Fifth message"),
    ]
    for msg in messages:
        print("Hello Server Sending you the %s" % msg.Text)
        yield msg


def send_message(stub):
    stub.SubscribeForSendMessages(generate_messages())
    print("Done")


def run():

    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:6000')

    # create a stub (client)
    stub = Analogy_pb2_grpc.AnalogyStub(channel)

    send_message(stub)



if __name__ == "__main__":
    run()