import pibrella
import time
import sys

if len(sys.argv) >= 2:
    duty_cycle = float(sys.argv[1])
    pibrella.output.e.pwm(50, duty_cycle)
    pibrella.output.f.pwm(50, duty_cycle)
    time.sleep(1)
    pibrella.output.e.stop()
    pibrella.output.f.stop()
else:
    print("Bad parameters. Usage: {0} <duty_cycle>".format(sys.argv[0]))

