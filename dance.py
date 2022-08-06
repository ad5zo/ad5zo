from time import sleep
from signal import pause
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pttpin = 17 # 11
uppin = 27  # 13
dnpin = 22  # 15
t2 = 0.1
t1 = 0.1
GPIO.setwarnings(False)
GPIO.setup( pttpin , GPIO.OUT )

while 1:
        GPIO.output( pttpin , GPIO.HIGH)
        sleep( t1 )
        GPIO.output( pttpin , GPIO.LOW)
        sleep( t2 )

        if( t1 > 1 ):
            t1 = 0.03
        else:
            t1 = t1 + 0.03
            
        if( t2 < 0.2):
            t2 = 1
        else:
            t2 = t2 - 0.17
