import json
import time
import random
import string
from kafka import KafkaProducer

# This is a producer with sensor id 102
sensor_id = 102
event_count = 100
interval = 1
kafka_host = 'localhost:9092'
kafka_topic = 'readings'

#Initialize Kafka
producer = KafkaProducer(bootstrap_servers=[kafka_host],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

count = 1
print("Sensor ID 102 - truck that stops frequently")
for i in range(0,event_count):
    try:
        reading = {}
        reading['event_id'] = random.randint(1,1000000)
        reading['sensor_id'] = sensor_id
        reading['speed'] = random.uniform(80,120)
        reading['fuel_efficiency'] = random.uniform(5,12)
        reading['latitude'] = 37.74504
        reading['longitude'] = -122.46538
        reading['ts'] = int(time.time())

        # print(reading)

        producer.send(kafka_topic, value=reading)
        print("[%s] records produced so far.",str(count))
        count = count + 1
        time.sleep(2)
    except:
        print("An error occurred while publishing current record. ID[%s]",str(count))
    finally:
        print("Total %s records produced"%str(count))


