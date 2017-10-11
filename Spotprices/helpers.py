import hashlib

from pykafka import KafkaClient
import pandas as pd
import json
import logging
import datetime

#start from here changing

def download_from_ftp(ftp,filename):
    logging.debug('Downloading csv file' + filename + 'from ftp')
    with open(filename, "wb") as f:
        ftp.retrbinary('RETR %s' % filename, f.write)
    logging.debug('Finished downloading csv file' + filename + 'from ftp')


def csv_to_json(filename):
    logging.debug('Converting csv file' + filename + 'to json')
    data = pd.read_csv(filename, skiprows=[0, 1], sep='|', index_col=False, names=['id','valuedate','value'])
    data['valuedate'] = pd.to_datetime(data.valuedate,format='%d.%m.%Y %H:%M:%S').dt.strftime("%Y-%m-%d %H:%M:%S")
    utc_datetime = datetime.datetime.utcnow()
    processed_time = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
    data['processed_time'] = processed_time
    json_records = data.to_json(orient='records',date_unit='s')
    print(json_records)
    logging.debug('Finished converting csv file' + filename + 'to json')
    return json_records


def produce_msg_to_kafka(bootstrap_server, topic, message):
    """
    Produce the input message to the given kafka topic
    :param message: JSON array containing the messages
    :type message: JSON String
    :param bootstrap_server: The location of the kafka bootstrap server
    :type bootstrap_server: String
    :param topic: The topic to which the message is produced
    :type topic: String
    """
    logging.info('tennet: Producing message to Kafka')
    # Setup the kafka producer
    client = KafkaClient(bootstrap_server)
    topic = client.topics[topic.encode()]
    producer = topic.get_producer(sync=True)
    records = json.loads(message)
    for record in records:
        # print(json.dumps(record).encode())
        hash_object = hashlib.md5(json.dumps(record).encode()).hexdigest()
        record = record.update({'uid': hash_object})
        producer.produce(json.dumps(record).encode())
    logging.info('SpotPrices: Finished producing message to Kafka')


