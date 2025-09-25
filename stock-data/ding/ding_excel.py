import requests
import json


class DingTalkAPI:
    # 静态常量 樊xx组织-樊xx用户
    unionid = "IKJe2IhYaZmJbWOviPnEiPMgiEiE"

    # 复盘v3
    fupan_workbook_id = "Exel2BLV5zRMpGM5Uvyb6EZKJgk9rpMq"

    @staticmethod
    def get_access_token():
        """
        获取钉钉访问令牌
        """

        url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
        headers = {
            "Host": "api.dingtalk.com",
            "Content-Type": "application/json"
        }
        payload = {
            "appKey": "dingz4vimrokzjrj0pd4",
            "appSecret": "4yiom3JqtpIXFUXioklIFh8w1MiYvejxJoFtkEGXnbVKlcSRYPsEJmyrGa6cZ27D"
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json().get("accessToken")

    @staticmethod
    def get_workbook_sheets(workbook_id, operator_id="system"):
        """
        获取指定工作簿中的所有工作表

        Args:
            workbook_id (str): 工作簿ID
            operator_id (str, optional): 操作者ID

        Returns:
            dict:  工作表列表
            id 工作表ID
            name 工作表名称
        """

        # 构建API URL
        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{workbook_id}/sheets"

        # 添加查询参数
        params = {}
        if operator_id:
            params["operatorId"] = operator_id

        # 获取访问令牌
        access_token = DingTalkAPI.get_access_token()

        # 设置请求头
        headers = {
            "x-acs-dingtalk-access-token": access_token,
            "Content-Type": "application/json"
        }

        # 发送GET请求
        response = requests.get(url, headers=headers, params=params)

        # 返回响应结果
        return response.json().get("value")

    @staticmethod
    def get_sheet_info(workbook_id, sheet_id):
        """
        Args:
            workbook_id (str): 工作簿ID
            operator_id (str, optional): 操作者ID

        Returns:
            dict:  工作表列表
            id 工作表ID
            name 工作表名称
        """

        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}"
        params = {"operatorId" : DingTalkAPI.unionid}
        headers = {
            "x-acs-dingtalk-access-token": DingTalkAPI.get_access_token(),
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()

    @staticmethod
    def update_dingtalk_sheet_cell(workbook_id, sheet_id, range_address, values,
                                   horizontal_alignments=None, number_format=None,
                                   background_colors=None, font_size=12, hyperlinks=None,
                                   vertical_alignments=None):
        """
        调用钉钉表格更新单元格的方法
        Args:
            workbook_id (str): 工作簿ID
            sheet_id (str): 工作表ID
            range_address (str): 单元格范围地址
            values (list[list[str]], optional): 单元格值
            horizontal_alignments (list[list[str]], optional): 水平对齐方式
            number_format (str, optional): 数字格式
            background_colors (list[list[str]], optional): 背景颜色
            font_sizes (list[list[int]], optional): 字体大小
            hyperlinks (list[list[dict]], optional): 超链接
            vertical_alignments (list[list[str]], optional): 垂直对齐方式

        Returns:
            dict: API响应结果
        """

        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/ranges/{range_address}"
        params = {"operatorId" : DingTalkAPI.unionid}
        headers = {
            "x-acs-dingtalk-access-token": DingTalkAPI.get_access_token(),
            "Content-Type": "application/json"
        }

        # 构建请求体
        payload = {}
        if values is not None:
            payload["values"] = values
        if horizontal_alignments is not None:
            payload["horizontalAlignments"] = horizontal_alignments
        if number_format is not None:
            payload["numberFormat"] = number_format
        if background_colors is not None:
            payload["backgroundColors"] = background_colors

        # 根据values的行列结构生成相同结构的font_sizes
        font_sizes = []
        for row in values:
            font_sizes.append([font_size] * len(row))
        payload["fontSizes"] = font_sizes
        if hyperlinks is not None:
            payload["hyperlinks"] = hyperlinks
        if vertical_alignments is not None:
            payload["verticalAlignments"] = vertical_alignments

        response = requests.put(url, headers=headers, params=params, data=json.dumps(payload))
        return response.json()

    @staticmethod
    def get_dingtalk_user_info(userid, language="zh_CN"):
        """
        获取钉钉用户信息

        Args:
            userid (str): 用户ID
            language (str, optional): 语言，默认为"zh_CN"

        Returns:
            dict: API响应结果，包含用户信息
        """

        # 获取访问令牌
        access_token = DingTalkAPI.get_access_token()

        # 构建API URL
        url = f"https://oapi.dingtalk.com/topapi/v2/user/get?access_token={access_token}"

        # 设置请求头
        headers = {
            "Content-Type": "application/json"
        }

        # 构建请求体
        payload = {
            "language": language,
            "userid": userid
        }

        # 发送POST请求
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # 返回响应结果
        return response.json()


def main():
    # 获取工作簿中的所有工作表示例
    # sheets = DingTalkAPI.get_workbook_sheets(DingTalkAPI.fupan_workbook_id, DingTalkAPI.unionid)
    # print(sheets)
    ssss = '[{"name": "总览", "id": "st-cfc9459b-14613"}, {"name": "总结", "id": "st-cfc9459b-14818"}, {"name": "题材", "id": "st-cfc9459b-14841"}, {"name": "风格", "id": "st-cfc9459b-14921"}, {"name": "风向标", "id": "st-cfc9459b-14936"}, {"name": "计划", "id": "st-cfc9459b-14944"}]'
    sheets = json.loads(ssss)
    zonglan_sheet_id = [sheet["id"] for sheet in sheets if sheet["name"] == "总览"][0]
    # sheet_info = DingTalkAPI.get_sheet_info(DingTalkAPI.fupan_workbook_id, zonglan_sheet_id)
    # {"frozenRowCount": 1, "lastNonEmptyRow": 49, "frozenColumnCount": 0, "visibility": "visible", "lastNonEmptyColumn": 29, "name": "\u603b\u89c8", "id": "st-cfc9459b-14613", "rowCount": 201, "columnCount": 41}
    values = [["2025-09-24"], ["2025-09-25"]]
    res = DingTalkAPI.update_dingtalk_sheet_cell(DingTalkAPI.fupan_workbook_id, zonglan_sheet_id, "A51:A52", values)
    print(json.dumps(res))

if __name__ == "__main__":
    main()