import json
import time
import random
import string
from kafka import KafkaProducer

# This is a producer with sensor id 103
sensor_id = 103
interval = 5
kafka_host = 'localhost:9092'
kafka_topic = 'readings'

#Initialize Kafka
producer = KafkaProducer(bootstrap_servers=[kafka_host],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

gps_coordinates = [
    [37.63858,-122.39781],
    [37.63841,-122.40157],
    [37.63910,-122.40483],
    [37.6445,-122.4061],
    [37.64897,-122.40656],
    [37.65466,-122.40684],
    [37.66111,-122.40307],
    [37.66796,-122.39441],
    [37.67400,-122.38962],
    [37.67774,-122.38828],
    [37.6861,-122.3898],
    [37.7038,-122.3939],
    [37.7271,-122.4023],
    [37.7584,-122.4049],
    [37.77254,-122.40653]
]

count = 1
print("Sensor ID 103 - truck with a GPS trace")
for coordinate in gps_coordinates:
    try:
        reading = {}
        reading['event_id'] = random.randint(1,1000000)
        reading['sensor_id'] = sensor_id
        reading['speed'] = random.uniform(80,120)
        reading['fuel_efficiency'] = random.uniform(10,20)
        reading['latitude'] = coordinate[0]
        reading['longitude'] = coordinate[1]
        reading['ts'] = int(time.time())

        # print(reading)

        producer.send(kafka_topic, value=reading)
        print("[%s] records produced so far.",str(count))
        count = count + 1
        time.sleep(interval)
    except:
        print("An error occurred while publishing current record. ID[%s]",str(count))
    finally:
        print("Total %s records produced"%str(count))


