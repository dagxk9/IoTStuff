import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600



def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    
    return

file = open('log.txt','w')

state = True

while state:

    read_ser=ser.readline()
    read_ser=read_ser.decode("utf-8")
    print(read_ser)
    
    if read_ser[:3] == "msg" :
        state = False
        temp = read_ser.split(',')
        
        for i in range(1,5):
            command = temp[i]
            if(int(temp[i]) <= 20 ):
                command ="DISTANCE TOO CLOSE ERROR"
                blink(11)
            
            file.write(str(i)+ " Distance " +command + '\n')
            print(command+'\n')
            
            
      
    


file.close()

GPIO.cleanup()






