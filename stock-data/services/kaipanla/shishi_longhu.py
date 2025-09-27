import json
import os

import requests
import time
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def store(file_name, data):
    data_dir = "C:/Users/fanyi/PycharmProjects/jf-stock-server/stock-data/data"

    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

headers = {
    'users-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; HD1910 Build/LMY48Z)',

}
url = 'https://apphq.longhuvip.com/w1/api/index.php'
datas = {
    'st': '60',
    'Order': '1',
    'a': 'RealRankingInfo_W8',
    'c': 'NewStockRanking',
    'PhoneOSNew': '1',
    'RStart': '0925',
    'apiv': 'w28',
    'Type': '1',
    'DeviceID': 'ffffffff-a05e-f5e5-ffff-ffffc6851f29',
    'Isst': '0',
    'Date': '',
    'Index': '0',
    'FilterMotherboard': '0',
    'Filter': '0',
    'Ratio': '6',
    'FilterTIB': '0',
    'FilterGem': '0',
    'REnd': '1500'
}
response = requests.post(url, headers=headers, data=datas, verify=False)
response.raise_for_status()
data1 = response.json()['list']
print(len(data1))
print(data1)

# 在for循环前清空三个txt文件
open('200_gegu_kaipanla.txt', 'w', encoding='utf-8').close()
open('200_gegu概念.txt', 'w', encoding='utf-8').close()
open('200_1.txt', 'w', encoding='utf-8').close()
open('200_2.txt', 'w', encoding='utf-8').close()

for row in data1:
    print(row[0] + ':' + row[1] + ' 价格:' + str(row[5]) + ' 涨幅:' + str(row[6]) + '% {}'.format(row[23]) + ' 主力净额:' + str(
        row[13]) + ' 板块:' + row[4] + '\n')

    # 将编码从gbk改为utf-8以避免中文乱码
    with open('200_gegu_kaipanla.txt', 'a+', encoding='utf-8') as file:
        file.write(row[0] + ':' + row[1] + ' 价格:' + str(row[5]) + ' 涨幅:' + str(row[6]) + '% {}'.format(row[23])
                   + ' 主力净额:' + str(row[13]) + ' 板块:' + row[4] + '\n')

    code = row[0]
    name = row[4]
    pd = row[23]
    long = row[-15]
    num = ''
    if code[0] == '3' or code[0] == '0':
        num = '0'
        hz = '.SZ'
    elif code[0] == '6':
        num = '1'
        hz = '.Sh'
    else:
        num = ''
        hz = ''
        pass

    print(num + '|' + code + hz + '|' + name)
    with open('200_gegu概念.txt', 'a+', encoding='utf-8') as f1:
        f1.write(num + '|' + code + hz + '|' + name + '\n')
    if pd.lstrip().rstrip():
        with open('200_1.txt', 'a+', encoding='utf-8') as ff1:
            ff1.write(num + '|' + code + hz + '|' + pd.lstrip().rstrip() + '\n')
    with open('200_2.txt', 'a+', encoding='utf-8') as f22:
        f22.write(num + '|' + code + '|' + hz + '|' + str(row[13]) + '\n')