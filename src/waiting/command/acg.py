import os
import random

from waiting.initialize import config
from waiting.message import send
from network import get


class acg_class:
    plugin = "bot"
    permission = "command.acg"

    @staticmethod
    def user_execute(c_type, msg_data):
        # 获取API
        api = config.random_agc_api
        # 生成随机数
        num = random.randint(config.random_agc_min, config.random_agc_max)
        api = api.replace("%num%", str(num))
        # 获取图片文件
        image_name = get.get_img(api, config.random_agc_cache)
        if image_name is None:
            # 获取图片出错
            send.group_msg("获取图片出错", True)
            return
        # 获取绝对路径
        current_directory = os.getcwd()
        file_uri = "file://" + current_directory + "/temp/images/" + image_name
        # 发送图片
        send.group_msg("[CQ:image,file=" + file_uri + ",id=40000]", "false")
