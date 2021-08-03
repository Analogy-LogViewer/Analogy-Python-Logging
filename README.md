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
	// Sends a greeting
	rpc SubscribeForPublishingMessages (stream AnalogyGRPCLogMessage) returns (AnalogyMessageReply);
	rpc SubscribeForConsumingMessages (AnalogyConsumerMessage) returns (stream AnalogyGRPCLogMessage);
}

// The request message containing the user's name.
message AnalogyGRPCLogMessage {
	string Text = 1;
	AnalogyGRPCLogLevel Level = 2;
	google.protobuf.Timestamp Date = 3;
	int32 ProcessId =4;
	int32 ThreadId =5;
	string Module =6;
	string Source = 7;
	string MethodName = 8;
	string FileName = 9;
	int32 LineNumber = 10;
	string MachineName=11;
	string Category = 12;
	string User =13;
	map<string,string> AdditionalInformation=14;
	string Id = 15;
	AnalogyGRPCLogClass Class=16;
}

// The response message containing the greetings.
message AnalogyMessageReply {
	string message = 1;
}
message AnalogyConsumerMessage {
	string message = 1;
	bool streamOldMessages=2;
}

enum AnalogyGRPCLogClass{
	GENERAL=0;
	/// <summary>
	/// Security logs (audit trails)
	/// </summary>
	SECURITY=1;
	/// <summary>
	/// Hazard issues
	/// </summary>
	HAZARD=2;
	//
	// Summary:
	//Protected Health Information
	PHI=3;
}

enum AnalogyGRPCLogLevel
{
	UNKNOWN=0;
	TRACE=1;
	VERBOSE=2;
	DEBUG=3;
	INFORMATION=4;
	WARNING=5;
	ERROR=6;
	CRITICAL=7;
	ANALOGY=8;
	NONE=9;
}

```
