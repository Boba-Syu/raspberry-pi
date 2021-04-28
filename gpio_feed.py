import RPi.GPIO as GPIO
import time


def setServoAngle(angle):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(32, GPIO.OUT)
    tilt = GPIO.PWM(32, 50)
    tilt.start(0)
    DutyCycle = angle / 18 + 2
    tilt.ChangeDutyCycle(DutyCycle)
    time.sleep(1)
    tilt.stop()


def feed():
    setServoAngle(90)


def feed_off():
    setServoAngle(0)


if __name__ == '__main__':
    c = input("If you want to continue, type 'c' please. Type 'e' to end.")
    while c == 'c':
        angle = input('Please type an angle:')  # input输入的是字符串，需要用int（）函数转化成数字。
        angle = int(angle)
        setServoAngle(angle)
        c = input("'c' or 'e'?")
    GPIO.cleanup()
    exit()
