import time
import datetime

filelist="file1.txt"
count=0
while count == 0:
    if "file.txt" in filelist:
        print("working fine")
        count=1
    else:
        time.sleep(30)
        print("no file going for sleep")
        count=0

filedate = str(datetime.date.today())
print(filedate)