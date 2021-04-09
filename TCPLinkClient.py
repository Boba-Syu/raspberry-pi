import socket
import logging
import threading


class TCPLinkClient(threading.Thread):
    def __init__(self, port: int = 8888):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.199.195' # socket.gethostname()
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
            break
        tcpLink.send(msg)
    tcpLink.close()
