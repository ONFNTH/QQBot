from waiting.initialize.config import address
from network import get
from file import log


# 向群聊发送聊天消息
# msg:String <消息内容>, escape:Boolean <消息内容是否作为纯文本发送(即不解析CQ码),只在msg是字符串时有效>
def group_msg(msg, group, escape):
    heads = {"group_id": str(group), "message": msg, "auto_escape": escape}
    get.heads_get_text(address + "/send_group_msg", heads)
    log.debug(f'发送消息{msg}', False)
