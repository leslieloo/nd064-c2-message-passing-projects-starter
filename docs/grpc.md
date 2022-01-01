## GRPC (Location Service)

The Location Service is reimplemented using grpc for message passing and store the received message into Kafka server. Later, the kafka message will be retrived by location consumer service and save into postgres database.

Module `modules/location_producer/client.py` to send sample requests (default 10 sample size) to grpc server (`modules/location_producer/server.py`).
The client.py use grpc to send message to gRPC server.ProtoBuf `location_event.proto` format is listed as below : 

```
message LocationMessage {
    int32 id = 1;
    int32 person_id = 2;
    string longitude = 3;
    string latitude = 4;
    string creation_time = 5;
}

service LocationService {
    rpc Create(LocationMessage) returns (LocationMessage);
}
```

To issue a sample request, use `kubecltl get pods` to get the pod_id (udaconnect-location-producer-xxxxx), and then run the following command:-
```
kubectl exec <location-producer-pod-id> -- python client.py 20
```
