# UdaConnect

### Architecture Diagrams : Message Passing Strategy

1. REST : The previous monolith REST api is break into 2 disintct API, Person & Connection API. Person API is used to retrieve and create person information, while Connection API is used to view a person connection. Both API is used by the frontend app.

2. gRPC : Mobile device will send location event (can be simulate by `location_producer/client.py`) to gRPC server hosted by producer service `location_producer/server.py`). The message passing strategy is chosen because of efficiency/high performance of data delivery between client (mobile device) and server (gRPC server)

3. Kafka : Kafka producer will be used to create kafka message from the mobile location events received by gRPC server (`location_producer/server.py`), and later processed by location consumer service (`location_consumer/app.py` )using kafka consumer and save it into postgres database.