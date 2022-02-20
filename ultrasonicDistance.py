import RPi.GPIO as GPIO
import time

#Initializations
triggerPin = 40
echoPin = 38
start = 0
stop = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)

GPIO.output(triggerPin,0)

while(1):
        #0.5 seconds delay between measurements
        time.sleep(0.5)

        #start reading from the trigger pin
        GPIO.output(triggerPin,1)
        time.sleep(10e-6)
        GPIO.output(triggerPin,0)

        while (GPIO.input(echoPin) == 0):
                start = time.time()

        while (GPIO.input(echoPin) == 1):
                stop = time.time()

        distance = 340.29e2 * (stop-start)/2
        print("Distance = ", distance, "cm")
