from kafka import KafkaProducer, KafkaConsumer
import pandas as pd
import json
import os

output_data_dir = "data/"

if __name__ == '__main__':
    consum = KafkaConsumer('fbpost',bootstrap_servers='localhost:9092')

    for message in consum:
        # Parse the decoded message as JSON
        parsed_json = json.loads(message.value.decode('utf-8'))
        
        output_json_path = os.path.join(output_data_dir, parsed_json['post_id']+'.json')
        with open(output_json_path, 'w') as json_file:
            json.dump(parsed_json, json_file)
            print("Saved done!")


        

        

    