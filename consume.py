import time

from  kafka_consumer import Consumer
from constants import BIKES_STATION_INFORMATION_TOPIC, BIKES_STATION_STATUS_TOPIC




class Consume:
    def __init__(self):
        self.consumer_group = Consumer('citi_bike_stations')

    def consume(self):
        while True:
            self.consumer_group.subscribe_consumer([BIKES_STATION_INFORMATION_TOPIC, 
                                                        BIKES_STATION_INFORMATION_TOPIC])

            for message in self.consumer_group.consumer:
                print(message.topic, message.partition, message.offset, message.value)
                self.consumer_group.rebalance_listener.add_offset(message.topic, message.partition, message.offset)
            self.consumer_group.consumer.commit(self.consumer_group.rebalance_listener.get_current_offsets)

consume_instance = Consume()
consume_instance.consume()

