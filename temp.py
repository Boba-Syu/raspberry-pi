import time

from databaseOperation import MysqlLink


def read_temperature():
    tfile = open("/sys/bus/w1/devices/28-01204419ecb5/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


if __name__ == '__main__':
    while True:
        temperature = read_temperature()
        print(temperature)
        mysql = MysqlLink()
        mysql.insert_temp(temperature=temperature)
        time.sleep(1)
