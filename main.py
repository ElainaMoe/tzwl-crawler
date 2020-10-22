import requests
import datetime
import csv
import os
import time

success=0
start_timestamp=time.time()
def create_csv(path):
    with open(path,"w+",newline="",encoding="utf8") as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = 'data' # 创建csv表头
        csv_file.writerow(head)
def append_csv(path):
    with open(path,"a+",newline='',encoding="utf8") as file:
        csv_file = csv.writer(file)
        data = [info]
        csv_file.writerows(data)

baseurl="http://tzwl.xyz/index/kminfo.html?ddid="
time = datetime.datetime.now()
date=str(time.year)+str(time.month)+str(time.day)
filename="./data/"+date+'.csv'
create_csv(filename)
for i in range(1,99999999999):
    url=baseurl+date+str(i).zfill(11)
    print(url)
    result=requests.get(url)
    info=result.text[1:]
    if str(info)=='[]':
        print('获取到空内容，舍弃……')
    else:
        print('获取到内容，正在存储……')
        success=1
        append_csv(filename)
    end_timestamp=time.time()
    if end_timestamp-start_timestamp>19800:
        break
if success == 0:
    os.remove(filename)
