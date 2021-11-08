from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

VALUE_SCHEMA_STR = """
{
   "namespace": "my.test",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

KEY_SCHEMA_STR = """
{
   "namespace": "my.test",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

value_schema = avro.loads(VALUE_SCHEMA_STR)
key_schema = avro.loads(KEY_SCHEMA_STR)
value = {"name": "Value"}
key = {"name": "Key"}


def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


avroProducer = AvroProducer(
    {
        "bootstrap.servers": "localhost:9092",
        "on_delivery": delivery_report,
        "schema.registry.url": "http://localhost:8081",
    },
    default_key_schema=key_schema,
    default_value_schema=value_schema,
)

avroProducer.produce(topic="my_topic", value=value, key=key)
avroProducer.flush()

print("Succesfully produced kafka message!")
