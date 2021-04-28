import time

import temp
from TCPLinkClient import TCPLinkClient
from databaseOperation import MysqlLink

if __name__ == '__main__':
    tcpLink = TCPLinkClient(6666)
    tcpLink.start()
    while True:
        temperature = temp.read_temperature()
        print(temperature)
        mysql = MysqlLink()
        mysql.insert_temp(temperature=temperature)
        time.sleep(10)
