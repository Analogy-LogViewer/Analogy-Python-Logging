# Analogy-Python-Logging
Example of how to send real time log messages from python to Analogy Log Server and view them in Analogy Log Viewer

basically, Just use the already generated Analogy_pb2.py and Analogy_pb2_grpc.py grpc code.

Here is example AnalogyClient.py file that sends dummy messages to Analogy Log Server


```python
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

```

To install Analogy Log Server Windows service download it from the [AnalogyLog Server release section](https://github.com/Analogy-LogViewer/Analogy.LogViewer.gRPC/releases/tag/V0.3.4) and install it as descripte in the release.
After that, Open Analogy Log Viewer, go to grpc tab and click on real time.


the proto file is:
```proto
syntax = "proto3";
import "timestamp.proto";

package greet;

// The greeting service definition.
service Analogy {
	rpc SubscribeForSendMessages (stream AnalogyLogMessage) returns (AnalogyMessageReply);
	rpc SubscribeForConsumeMessages (AnalogyConsumerMessage) returns (stream AnalogyLogMessage);
}

// The request message containing the user's name.
message AnalogyLogMessage {
	string Id = 1;
	google.protobuf.Timestamp Date = 2;
	string Text =3;
	string Category =4;
	string Source =5;
	string MethodName =6;
	string FileName =7;
	int32 LineNumber =8;
	string Class=9;
	string MachineName=10;
	string Level=11;
	string Module =12;
	int32 ProcessId =13;
	int32 ThreadId =14;
	string User =15;
	map<string,string> AdditionalInformation=16;
}

// The response message containing the greetings.
message AnalogyMessageReply {
	string message = 1;
}
message AnalogyConsumerMessage {
	string message = 1;
}
```
