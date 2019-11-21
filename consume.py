from  kafka_consumer import Consumer
from constants import BIKES_STATION_INFORMATION_TOPIC, BIKES_STATION_STATUS_TOPIC

consumer_group = Consumer('citi_bike_stations')
while True:
    consumer_group.subscribe_consumer([BIKES_STATION_INFORMATION_TOPIC, 
                                                BIKES_STATION_INFORMATION_TOPIC])

    for message in consumer_group.consumer:
        print(message.topic, message.offset, message.partition, message.value)
