import logging
import logging.handlers
from custom_logstash import LogstashFormatter,LogstashHandler
import csv
import json
from ftplib import FTP
import pandas as pd
import settings
import helpers
import sys
import datetime

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = LogstashHandler('swarm-master-BE117DBE-0', 4512, ssl=False)
formatter = LogstashFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

def run():
    #filedate = str(datetime.date.today())
    logger.debug('reuters_spotprices history_NL data downloading')
    ftp = FTP(settings.FTP_HOST, settings.FTP_USER, settings.FTP_PASS)
    ftp.cwd(settings.FTP_FILE_PATH)
    files_prefix=settings.FILES_PREFIX
    for file_prefix in files_prefix:
        filename = file_prefix + ".CSV"
        helpers.download_from_ftp(ftp, filename)
        json_records=helpers.csv_to_json(filename)
        helpers.produce_msg_to_kafka(settings.BOOTSTRAP_SERVER, settings.KAFKA_TOPIC, json_records)
    ftp.close()
    logger.debug('reuters_spotprices_NL live data downloaded')

if __name__ == '__main__':
        try:
            logging.debug('Spot Prices Process started')
            run()
            logging.debug('Spot prices Process finished')
            sys.exit(0)
        except Exception as err:
           logging.error('Spot_prices_NL:Process caught with error')
           sys.exit(1)
            #logger.info(traceback)
            # helpers.post_slack_message(errors)


















