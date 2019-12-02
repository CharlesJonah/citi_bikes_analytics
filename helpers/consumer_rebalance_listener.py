from kafka import ConsumerRebalanceListener
from kafka import TopicPartition
from kafka.structs import OffsetAndMetadata
current_offsets = {}

class ConsumerRebalanceListenerHandler(ConsumerRebalanceListener):
    def __init__(self, consumer):
        self.consumer = consumer

    def get_current_offsets(self):
        return current_offsets

    def add_offset(self, topic, partition, offset):
        key = TopicPartition(topic,partition)
        current_offsets[key] = OffsetAndMetadata(offset, 'commit')

    def on_partitions_revoked(self, revoked):
        self.consumer.commit(self.get_current_offsets)
        current_offsets = {}
         
    
    def on_partitions_assigned(self, assigned):
        pass



    