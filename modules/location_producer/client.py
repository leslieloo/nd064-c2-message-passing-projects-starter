import logging
import argparse
import random

import grpc
import location_pb2
import location_pb2_grpc

from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-producer-sample")


channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="sample size to generate sample message", nargs='?', type=int, default=10)
    return parser.parse_args()

def gen_sample_data(size=10):
    logger.info("Sending sample payload...")

    for i in range(size):

        location = location_pb2.LocationMessage(
            person_id=random.choice([1, 5, 6, 8, 9]),
            longitude="{:.4f}".format(random.uniform(80, 100)),
            latitude="{:.4f}".format(random.uniform(80, 100)),
            creation_time=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        )

        response = stub.Create(location)
        logger.info(location)

if __name__ == "__main__":
    args = parse_args()
    gen_sample_data(args.size)