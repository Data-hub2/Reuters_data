# FTP site parameters
FTP_HOST = "pointconnect.commodities.thomsonreuters.com"
FTP_USER = "Data_Eneco"
FTP_PASS = "351EnD"

# FTP folder parameters for live data
#FTP_FILE_PATH = "/PCO_Eneco/PCO_Eneco/Live/Prices"
#FILES_PREFIX=["5059255_Pwr_APX-Endex_PriVol_DA_NLD_A_"]

#FTP folder parameters for history data
FTP_FILE_PATH="/PCO_Eneco/PCO_Eneco/History/Prices"
FILES_PREFIX=["5059256_HIST_Pwr_APX-Endex_PriVol_DA_NLD_A_2017","5059256_HIST_Pwr_APX-Endex_PriVol_DA_NLD_A_2016"]

# Kafka Bootstrap server settings
BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "Spot_prices"

#SLEEPER_TIME = 60