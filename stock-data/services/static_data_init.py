from xtquant import xtdata
import json
import os

# 获取沪深两市的最新行情快照
# snapshot = xtdata.get_full_tick(["SH", "SZ"])
#
# # 打印数据
# print(f"当前市场共{len(snapshot)}只股票")
# if snapshot:
#     # 展示第一只股票的数据
#     print(snapshot["002295.SZ"])
#     first_stock = list(snapshot.keys())[0]

data_dir = "C:/Users/fanyi/PycharmProjects/jf-stock-server/stock-data/data"
file_path = os.path.join(data_dir, "stock_codes.json")

codes = xtdata.get_stock_list_in_sector('沪深A股')
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(codes, f, ensure_ascii=False, indent=2)

print(f"拉取到沪深A股共{len(codes)}只股票")