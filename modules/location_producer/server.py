import time
import logging
import json
import os
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-producer")

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request: location_pb2, context):
        logger.info("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        logger.info(request_value)

        producer.send(KAFKA_TOPIC, json.dumps(request_value).encode('utf-8'))
        producer.flush()

        return location_pb2.LocationMessage(**request_value)


producer = KafkaProducer(bootstrap_servers=KAFKA_URL)

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


logger.info("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
