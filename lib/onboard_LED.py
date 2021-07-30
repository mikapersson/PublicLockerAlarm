import pycom
import time

def LED_off():
    pycom.heartbeat(False)

def LED_sleeping():
    pycom.rgbled(0xFF00FF)

def LED_alarm():
    pycom.rgbled(0xFF0000)