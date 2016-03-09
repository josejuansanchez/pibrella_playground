import pibrella
import time

pibrella.output.e.pwm(50, 7)
time.sleep(1)

pibrella.output.e.duty_cycle(5)
time.sleep(1)

pibrella.output.e.duty_cycle(10)
time.sleep(1)

pibrella.output.e.stop()

