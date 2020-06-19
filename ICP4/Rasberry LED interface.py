import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600


def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
    read_ser=ser.readline()
    command=read_ser.decode("ASCII");
    print(command)
    if(command.strip() == "Hello From Arduino!"):
            
        blink(11)
    