from command import help, send


def execute(c_type):
    # 转换为数组
    arr_type = c_type.split()
    if arr_type[0] == "help":
        help.execute(arr_type)
    if arr_type[0] == "send":
        send.execute(arr_type)
    else:
        print("无效的命令")
