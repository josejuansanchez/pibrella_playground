# Reference: Paul McWhorter
# https://www.youtube.com/watch?v=SGwhx1MYXUs

import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7)

delay = 0.05

try:
    while(1):
        for i in range(0, 180):
	    dc = 1/18. * i + 2
            pwm.ChangeDutyCycle(dc)
	    time.sleep(delay)
	    print("DutyCycle: {0}".format(dc))

        for i in range(180, 0, -1):
	    dc = 1/18. * i + 2
	    pwm.ChangeDutyCycle(dc)
	    time.sleep(delay)
	    print("DutyCycle: {0}".format(dc))
except KeyboardInterrupt:
    print("Error: KeyboardInterrupt")
    pass
finally:
    print("Finally")
    pwm.stop()
    GPIO.cleanup()
