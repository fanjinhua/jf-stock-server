import sys
import os

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from fastapi import FastAPI
from ding.ding_robot import DingRobotPusher

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
    
    
@app.post("/send-ding-message")
async def send_ding_message(message: str):
    """
    发送钉钉行情消息接口
    
    :param message: 消息内容
    :return: 发送结果
    """
    pusher = DingRobotPusher()
    result = pusher.send_hang_qing_msg(message)
    return result
