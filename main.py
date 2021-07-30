from lib.onboard_LED import LED_alarm, LED_off, LED_sleeping
from lib.buzzer import play_alarm
from buzzer import play_alarm
from pir import test_pir, pir_input
from machine import Pin
import time
from onboard_LED import *


""" Main Code """
LED_off()

print("Sleeping")
LED_sleeping()
time.sleep(10)  # sleep for ten seconds, this gives enough time to close the locker
# IDEA: Talk to the pycom through a phone in order to determine if the alarm should be ready or not
LED_off()

# Some constants
pir_pin = Pin("P4", mode=Pin.IN)
#time_frame = 
detections = []  # detections during time frame, makes detection more robust

# Main Loop
while True:
    # Check the input from the PIR sensor
    print("Streak: ", len(detections))
    motion_detected = pir_pin()

    # If the PIR sensor detects motion, the alarm goes of and a notification is sent to the owner
    if motion_detected:
        print("DETECTED SOMETHING")
        detections.append(True)
        LED_alarm()

        # If detection streak is 2 or more
        if len(detections) > 0:  # changed from 1 to 0 because the alarm was not triggered during the testing
            # Sending data through sigfox to Pybytes and then to IFTTT through webhook
            pybytes.send_signal(3, motion_detected)
            print("Sent detection to Pybytes")

            # Play alarm
            play_alarm()
        
        LED_off()
    else:
        # Reset detection streak
        detections = []
    
    time.sleep(2)

    
# Test buzzer
# play_alarm()

# Testing PIR
# test_pir()

# Test wifi
"""
while True:
    #The value can be a sensor reading being done here
    value = 5

    #Sending to pybytes in channel 1
    pybytes.send_signal(3, value)
    print("sending: {}".format(value))
    
    #Send every 5 seconds
    time.sleep(5)
"""

# Test Sigfox (https://hackmd.io/@lnu-iot/SyUxJU7pu)
# Below is the code snippet that runs after configuring the Sigfox backend, 
# one only need to call the function 'pybytes.send_signal(channel, value)'
"""
while True:
    #Select a value to send, 
    #perhaps before this you've read from a sensor
    value = 5
    
    #Send the value
    pybytes.send_signal(1, value)
    print("sending: {}".format(value))
    
    #Sending data once every 11 minutes 
    time.sleep(5) 
"""
