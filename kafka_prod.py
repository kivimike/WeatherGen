from kafka import KafkaProducer
from csv import DictReader
import json
bootstrap_servers = ['localhost']
topicname = 'test.salesdata'
# producer = KafkaProducer(bootstrap_servers = bootstrap_servers,api_version=(0,1,0))
#producer = KafkaProducer()

with open('hello','r') as read_obj:
     csv_dict_reader = DictReader(read_obj)
     for row in csv_dict_reader:
          print(row)
          break
          #ack = producer.send(topicname, json.dumps(row).encode('utf-8'))
          #result = ack.get()
          #print(result)