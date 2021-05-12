import os


def open_fan():
    """
    给树莓派发送shell指令, 打开风扇
    :return: shell指令的返回值
    """
    return os.system('sudo gpio write 15 1')


def stop_fan():
    """
    给树莓派发送shell指令, 关闭风扇
    :return: shell指令的返回值
    """
    return os.system('sudo gpio write 15 0')
