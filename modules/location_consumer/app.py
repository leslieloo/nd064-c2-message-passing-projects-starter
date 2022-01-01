import os
import json
import logging
import app
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-consumer")


def run_app(env=None):
    config = app.init_env(env)
    consumer = KafkaConsumer(config.KAFKA_TOPIC, bootstrap_servers=config.KAFKA_URL, group_id="udaconnect-location-consumer")

    from app.udaconnect.services import LocationService as svc, Location

    while (True):
        for msg in consumer:
            loc_msg = json.loads(msg.value.decode('utf-8'))
            logger.info(loc_msg)

            location:Location = svc.create(loc_msg)

if __name__ == "__main__":
    run_app(os.getenv("FLASK_ENV") or "test")


