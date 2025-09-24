
from push.ding_robot import DingRobotPusher

if __name__ == "__main__":
    pusher = DingRobotPusher()
    result = pusher.send_hang_qing_msg("测试2222消息：发送")
    print(result)