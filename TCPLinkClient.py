#!/usr/bin/env python
# coding=utf-8

import socket
import logging
import threading

import motion
from InstructionEnum import InstructionEnum


class TCPLinkClient(threading.Thread):
    """
    使用TCP连接服务器的
    """

    def __init__(self, port: int = 8888):
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
                elif msg == str(InstructionEnum.CLOSE_MOTION):
                    logging.info('关闭摄像头')
                    motion.stop_motion()

    def send(self, data: str):
        self.socket.send(data.encode(encoding='utf-8'))

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    tcpLink = TCPLinkClient(8888)
    tcpLink.start()
    while True:
        msg = input()
        if msg == 'quit':
            tcpLink.close()
            break
        tcpLink.send(msg)
