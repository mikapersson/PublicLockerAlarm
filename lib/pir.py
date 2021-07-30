# File for managing the PIR sensor
# Inspiration from https://docs.pycom.io/tutorials/hardware/pir/
from machine import Pin
import time

def test_pir():
    #config
    hold_time_sec = 10

    #flags
    last_trigger = -10

    pir_pin = Pin("P4", mode=Pin.IN)

    while True:
        if pir_pin() == 1:  # If motion has been detected
            if time.time() - last_trigger > hold_time_sec:
                last_trigger = time.time()
                print("DETECTED SOMETHING!")
        else:
            last_trigger = 0
            print("No presence")

        time.sleep_ms(500)

def pir_input(pir_pin):
    return pir_pin()