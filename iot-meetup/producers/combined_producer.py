import json
import time
import random
import string
from kafka import KafkaProducer

event_count = 100
kafka_host = 'localhost:9092'
kafka_topic = 'readings'

#Initialize Kafka
producer = KafkaProducer(bootstrap_servers=[kafka_host],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

count = 1
print("Starting fleet simulator...")
for i in range(0,event_count):
    try:
        reading = {}
        reading['event_id'] = random.randint(1,1000000)
        reading['sensor_id'] = random.randrange(100, 105)
        reading['speed'] = random.uniform(0, 1) * 180
        reading['latitude'] = random.uniform(0, 1) * 200
        reading['longitude'] = random.uniform(0, 1) * 200
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


