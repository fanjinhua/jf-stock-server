import time

import requests
import json
import datetime as dt
import pandas as pd


kpl_headers = {
    'User-Agent': 'lhb/5.2.9 (com.kaipanla.www; build:0; iOS 15.1.0) Alamofire/5.2.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept-Language': 'zh-Hans-CN;q=1.0, bo-CN;q=0.9, ar-CN;q=0.8',
    'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5'
}

def kpl_getZT():
    data={
        'Index': '0', 'Is_st': '1', 'Order': '1', 'PhoneOSNew': '2', 'PidType': '1', 'Type': '6', 'VerSion': '5.2.0.9',
        'a': 'DaBanList', 'apiv': 'w28', 'c': 'HomeDingPan', 'st': '60'
    }
    url='https://apphq.longhuvip.com/w1/api/index.php'
    resp = requests.post(url=url, headers=kpl_headers, verify=False, data=data)
    ret = resp.text.encode('utf-8').decode('unicode-escape')
    js_data = json.loads(ret)
    ret = js_data['list']
    day = js_data['day']
    ret = pd.DataFrame(ret)
    ret = ret.iloc[:,[0,1,4,9,10,13,16,17,18,22,25,27]]
    ret.columns = ['code', 'name', 'quote_change', 'last_tj', 'limit_times', 'volume', 'industry', 'latest_price', 'first_limit', 'limit_money', 'last_limit', 'industry_limits_num']
    ret.first_limit = ret.first_limit.apply(lambda x: dt.datetime.fromtimestamp(x).strftime("%H%M%S"))
    ret.last_limit = ret.last_limit.apply(lambda x: dt.datetime.fromtimestamp(x).strftime("%H%M%S"))
    print(ret, day)
    return day, ret


def stat_zt_kpl(tmp_datetime):
    datetime_str = '2025-09-26' # (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = '2025-09-26' # (tmp_datetime).strftime("%Y%m%d")
    print("datetime_int: {}".format(datetime_int))
    url='https://apphis.longhuvip.com/w1/api/index.php'
    col = {
        0 : 'code',
        1 : 'name',
        6 : 'first_limit',
        8 : 'limit_money',
        9 : 'last_tj',
        10 : 'limit_times',
        16: 'industry',
        25: 'last_limit',
        24: 'break_times',
        15: 'floating_market',
        27: 'industry_limits_num',
    }

    for ztType in range(0, 3):
        zt_df = None
        index = 0
        trunk = 60
        while True:
            '''
            PidType : 1  --- zt list
            PidType : 2  --- zb list
            PidType : 3  --- dt list
            '''
            data = {
                    "Order" : "1",
                    "a" : "HisDaBanList",
                    "st" : f"{trunk}",
                    "c" : "HisHomeDingPan",
                    "PhoneOSNew" : "1",
                    "DeviceID" : "960c85fe-a145-3c06-a63c-b6b9f8525460",
                    "VerSion" : "5.11.0.6",
                    "Index" : f"{index}",
                    "Is_st" : "1",
                    "PidType" : f"{ztType + 1}",
                    "apiv" : "w33",
                    "Type" : "6",
                    "FilterMotherboard" : "0",
                    "Filter" : "0",
                    "FilterTIB" : "0",
                    "Day" : f"{datetime_str}",
                    "FilterGem" : "0",
            }
            resp = requests.post(url=url, headers=kpl_headers, verify=False, data=data)
            ret = resp.text.encode('utf-8').decode('unicode-escape')
            df = pd.DataFrame(json.loads(ret)['list'])
            if df.empty:
                break
            zt = pd.DataFrame()
            for idx in col.keys():
                zt[col.get(idx)] = df.loc[:, [idx]]
            zt['first_limit'] = zt.first_limit.apply(lambda x: time.strftime("%H%M%S", time.localtime(x)))
            zt['last_limit'] = zt.last_limit.apply(lambda x: time.strftime("%H%M%S", time.localtime(x)))
            zt = zt.reset_index(drop=True)
            if zt_df is None:
                zt_df = zt
            else:
                zt_df = pd.concat([zt_df, zt])
            if df.shape[0] < trunk:
                break
            else:
                index += trunk
        if zt_df is None:
            continue
        print(zt_df)
        zt_df['date'] = datetime_int
        zt_df = zt_df.reset_index(drop=True)
        zt_df = zt_df.set_index('code')
        zt_df['flag'] = ztType
        zt_df['quote_change'] = 0
        zt_df['volume'] = 0
        zt_df['latest_price'] = 0
        zt_df['turnover_rate'] = 0
        zt_df['kpl_reason'] = ""
        zt_df['thx_reason'] = ""
        zt_df['total_market'] = 0

    return None

stat_zt_kpl(dt.datetime.now())