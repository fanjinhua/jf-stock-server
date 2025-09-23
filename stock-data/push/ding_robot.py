import requests
import json
from enum import Enum


class DingRobotEnum(Enum):
    """钉钉机器人枚举类"""
    """行情触达"""
    HANG_QING_DA_TA = "https://oapi.dingtalk.com/robot/send?access_token=fdbbc60890d42484b90e02a94ebde4549423a7e8ce63cf66ccf38a4150d24cd5"
    OTHER_ROBOT = "https://oapi.dingtalk.com/robot/send?access_token=other_token"


class DingRobotPusher:
    def __init__(self):
        """
        初始化钉钉消息推送类
        """
        pass

    def send_hang_qing_msg(self, message_text: str) -> dict:
        """
        发送消息到行情触达钉钉机器人
        
        :param message_text: 消息文本
        :return: 返回响应结果
        """
        robot_url = DingRobotEnum.HANG_QING_DA_TA.value
        return self._send_message(robot_url, message_text)

    def send_other_msg(self, message_text: str) -> dict:
        """
        发送消息到其他钉钉机器人
        
        :param message_text: 消息文本
        :return: 返回响应结果
        """
        robot_url = DingRobotEnum.OTHER_ROBOT.value
        return self._send_message(robot_url, message_text)

    def _send_message(self, robot_url: str, message_text: str) -> dict:
        """
        发送消息到钉钉机器人
        
        :param robot_url: 机器人URL
        :param message_text: 消息文本
        :return: 返回响应结果
        """
        headers = {'Content-Type': 'application/json'}
        payload = {
            "msgtype": "text",
            "text": {
                "content": message_text
            }
        }
        
        try:
            response = requests.post(robot_url, headers=headers, data=json.dumps(payload))
            return response.json()
        except Exception as e:
            return {"error": str(e)}