from fastapi import FastAPI
from push.ding_robot import DingRobotPusher

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

if __name__ == "__main__":
    pusher = DingRobotPusher()
    result = pusher.send_hang_qing_msg("测试消息发送")