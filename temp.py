import time


def read_temperature():
    tfile = open("/sys/bus/w1/devices/28-000004d618fa/w1_slave")
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
        time.sleep(1)
