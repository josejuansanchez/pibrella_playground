# burglar alarm! (catches grinches and gruffalos)
import pibrella, signal

def alarm(pin): 
   pibrella.buzzer.fail()        # make some noise
   pibrella.light.pulse()        # flash lights

def reset(pin):
   pibrella.light.stop()         # reset alarm

pibrella.input.a.changed(alarm)  # listen for intruder
pibrella.button.pressed(reset)   # in case of stupid cat

signal.pause()                   # waiting for intruder!
