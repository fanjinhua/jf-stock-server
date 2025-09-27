from xtquant import xtdata
import json
import os

# xtdata.enable_hello = False
# 获取沪深两市的最新行情快照
# snapshot = xtdata.get_full_tick(["SH", "SZ"])
#
# # 打印数据
# print(f"当前市场共{len(snapshot)}只股票")
# if snapshot:
#     # 展示第一只股票的数据
#     print(snapshot["002295.SZ"])
#     first_stock = list(snapshot.keys())[0]


def store(file_name, data):
    data_dir = "C:/Users/fanyi/PycharmProjects/jf-stock-server/stock-data/data"

    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_stock_codes():
    codes = xtdata.get_stock_list_in_sector('沪深A股')
    store("stock_codes.json", codes)
    print(f"拉取到沪深A股共{len(codes)}只股票")

def fetch_stock_sectors():
    '''     获取板块    '''
    all_sectors = xtdata.get_sector_list()
    store("stock_sectors.json", all_sectors)
    print(f"拉取到{len(all_sectors)}个板块")

def fetch_full_codes():
    '''     获取板块    '''
    # snapshot = xtdata.get_full_tick(["SH", "SZ"])
    snapshot = xtdata.get_full_tick(["SW"])
    store("full_codes.json", list(snapshot.keys()))
    print(f"拉取到{len(snapshot.keys())}个标的")

def get_local_data():
    pass

def main():
    # fetch_stock_codes()
    # fetch_stock_sectors()
    # fetch_full_codes()

    xt_sector_index_list = xtdata.get_stock_list_in_sector("迅投一级行业板块加权指数")
    print(xt_sector_index_list)

    # 获取迅投板块指数合约信息
    # xt_sector_index_info = xtdata.get_instrument_detail(xt_sector_index_list[0])
    # xt_sector_index = xt_sector_index_list[0]
    # print(xt_sector_index_info)

    # xtdata.get_stock_name()
    # codes = xtdata.get_stock_list_in_sector('上证消费')
    # print(codes)
    # 上证消费
    # snapshot = xtdata.get_full_tick(['000036.SH'])
    # # xtdata.get_sector('000036.SH')
    # print(snapshot)

if __name__ == "__main__":
    main()