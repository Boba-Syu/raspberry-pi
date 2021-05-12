#!/usr/bin/env python
# coding=utf-8

import socket
import logging
import threading

import gpio_feed
import motion
from InstructionEnum import InstructionEnum
import  gpio_fan

class TCPLinkClient(threading.Thread):
    """
    使用TCP连接服务器的
    """

    def __init__(self, port: int = 6666):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '81.68.230.143'  # socket.gethostname()
        # self.host = '127.0.0.1'  # socket.gethostname()
        self.port = port
        try:
            self.socket.connect((self.host, self.port))
        except Exception:
            logging.info('端口号{}连接失败.'.format(self.port))
        logging.info('端口号{}连接失败.'.format(self.port))

    def run(self):
        while True:
            data = self.socket.recv(1024)
            if data:
                msg = bytes.decode(data, encoding='utf-8')
                print(msg)
                if msg == str(InstructionEnum.OPEN_MOTION.value):
                    logging.info('打开摄像头')
                    motion.open_motion()
                elif msg == str(InstructionEnum.CLOSE_MOTION.value):
                    logging.info('关闭摄像头')
                    motion.stop_motion()
                elif msg == str(InstructionEnum.FEED.value):
                    logging.info('喂食')
                    gpio_feed.feed()
                elif msg == str(InstructionEnum.FEED_OFF.value):
                    logging.info('停止喂食')
                    gpio_feed.feed_off()
                elif msg == str(InstructionEnum.HEAT_DOWM.value):
                    logging.info("风扇开")
                    gpio_fan.open_fan()
                elif msg == str(InstructionEnum.HEAT_UP.value):
                    logging.info("风扇关")
                    gpio_fan.stop_fan()

    def send(self, data: str):
        self.socket.send(data.encode(encoding='utf-8'))

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    tcpLink = TCPLinkClient(6666)
    tcpLink.start()
    while True:
        msg = input()
        if msg == 'quit':
            tcpLink.close()
            break
        tcpLink.send(msg)
