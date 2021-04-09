import os


def open_motion():
    """
    给树莓派发送shell指令, 开启摄像头
    :return: shell指令的返回值
    """
    return os.system('sudo motion')


def stop_motion():
    """
    给树莓派发送shell指令, 关闭摄像头
    :return: shell指令的返回值
    """
    return os.system('sudo killall -TERM motion')
