import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7)

try:
    # 90 - Center
    pwm.ChangeDutyCycle(7.5)
    time.sleep(1)

    # 0
    pwm.ChangeDutyCycle(5)
    time.sleep(1)

    # 180
    pwm.ChangeDutyCycle(10)
    time.sleep(1)
except KeyboardInterrupt:
    print("Error: KeyboardInterrupt")
    pass
finally:
    print("Finally")
    pwm.stop()
    GPIO.cleanup()
