#文件存储
import requests
response = requests.get('www.badu.com')
#1txt存储

with open('name.txt','w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))

#2json文件存储
#json类型的不能直接存储，需要转换成 str

import json

json.dumps(data)#将字典或者列表转换成str
json.loads(str)#将str 转换成 字典或者列表
#能写入文件的只能是 str

#3 csv文件存储
#写入
import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')#初始化写入对象,可以指定分隔符默认,
    writer.writerow(['id','name','age'])
    writer.writerow(['01','mike','20'])
    #可以写入多行，参数是二维列表

#字典的写入方式
import csv
with open('data.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()#写入头信息
    writer.writerow({'id':'01','name':'mike','age':'20'})
    #追加 打开模式修改为 a即可

#读取
import csv
with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    #如果包含中文需要指定文件编码
#另外可以利用pandas
import pandas as pd
df = pd.read_csv('data.csv')
print(df)