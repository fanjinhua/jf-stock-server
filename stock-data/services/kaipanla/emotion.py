import requests
import json
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 获取板块异动原因
block_boom_url = ('https://apphq.longhuvip.com/w1/api/index.php?a=GetBaseFaceListZDEvnArtNew&c=ZhiShuL2Data&PhoneOSNew=1'
       '&DeviceID=ffffffff-e91e-5efd-ffff-ffffa460846b&VerSion=5.11.0.6&apiv=w33&StockID=801199&')

# 情绪值
emotion_value_url = ('https://apphis.longhuvip.com/w1/api/index.php?a=DiskReview&apiv=w31&c=HisHomeDingPan&PhoneOSNew=1'
 '&DeviceID=00000000-296c-20ad-0000-00003eb74e84&VerSion=5.7.0.12&Day=2025-09-25&')

# 情绪指标, 强度，涨停家数，大幅回撤，
emotion_index_url = ('https://apphq.longhuvip.com/w1/api/index.php?a=ChangeStatistics&apiv=w33&c=HomeDingPan&PhoneOSNew=1&UserID=497432&DeviceID=ffffffff-e91e-5efd-ffff-ffffa460846b'
                     '&VerSion=5.11.0.6&') #Token=4761ad40037d3c58725b7966dbcbfdd2&')

# 情绪指标
emotion_index_history_url = ('https://apphis.longhuvip.com/w1/api/index.php?a=ChangeStatistics&apiv=w33&c=HisHomeDingPan&PhoneOSNew=1&UserID=497432&DeviceID=ffffffff-e91e-5efd-ffff-ffffa460846b'
                             '&VerSion=5.11.0.6&Token=4761ad40037d3c58725b7966dbcbfdd2&Day=2025-09-26')

# 打板竞价
daban_jingjia_url = ('https://apphq.longhuvip.com/w1/api/index.php?Order=1&a=DaBanList&st=60&c=HomeDingPan&PhoneOSNew=1&DeviceID=20ad85ca-becb-3bed-b3d4-30032a0f5923&Type=18&index=0&PidType=8&FilterMother=0&Filter=0'
                     '&FilterTIB=0&FilterGem=0&Day=2025-09-26')
# 赚钱效应，题材
zhuanqian_url = ('https://apphq.longhuvip.com/w1/api/index.php?c=StockFengKData&a=GetFengKListBest&Time=')

# 实时龙虎榜，第一页index为0，第二页index为60，第二页为120，第n页为（n-1)*60
# Order 0 是升序，1是降序
now_longhu_url = ('https://apphq.longhuvip.com/w1/api/index.php?Order=1'
                  '&a=RealRankingInfo_W8&st=15&c=NewStockRanking&PhoneOSNew=1'
                  '&RStart=0925&DeviceID=20ad85ca-becb-3bed-b3d4-30032a0f5923&VerSion=5.8.0.2&'
                  'index=0'
                  '&REnd=1500&apiv=w29&Type=18'
                  '&FilterMotherboard=0&Filter=0&Ratio=6&FilterTIB=0&FilterGem=0'
                  '&Date=')

try:
    response = requests.get(now_longhu_url, verify=False)  # 忽略SSL证书验证
    response.raise_for_status()
    data = response.json()
    data1 = response.json()['list']
    for row in data1:
        print(row[0] + ' ' + row[1])
    # json_output = json.dumps(data, indent=4, ensure_ascii=False)
    # print(json_output)
except requests.RequestException as e:
    print(f"请求出错: {e}")
except ValueError as e:
    print(f"解析 JSON 出错: {e}")