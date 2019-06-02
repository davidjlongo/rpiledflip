'''
Taken from clanger9
https://raspberrypi.stackexchange.com/questions/70013/raspberry-pi-3-model-b-system-leds/70017
'''

import os

green_led = "/sys/class/leds/led0"
red_led = "/sys/class/leds/led1"
green_led_reset_trigger = "mmc0"
red_led_reset_trigger = "input"

def control(led_colour, state):
    if led_colour == "green":
        device = green_led

    elif led_colour == "red":
        device = red_led

    else:
        return

    if  state == "on":
#        os.system("echo none | tee " + device + "/trigger >> /dev/null")
#        os.system("echo 1 | tee " + device + "/brightness >> /dev/null") 
        os.system("echo none >> " + device + "/trigger")
        os.system("echo 1 >> " + device + "/brightness") 

    elif state == "off":
#        os.system("echo none | tee " + device + "/trigger >> /dev/null")
#        os.system("echo 0 | tee " + device + "/brightness >> /dev/null") 
        os.system("echo none >> " + device + "/trigger")
        os.system("echo 0 >> " + device + "/brightness") 

    elif state == "flash":
        os.system("echo timer | tee " + device + "/trigger >> /dev/null")
        os.system("echo 1 | tee " + device + "/brightness >> /dev/null")

    elif state == "reset":
        if device == green_led:
            trigger = green_led_reset_trigger
        elif device == red_led:
            trigger = red_led_reset_trigger

        os.system("echo " + trigger + " | tee " + device + "/trigger >> /dev/null")
        os.system("echo 1 | tee " + device + "/brightness >> /dev/null") 

    else:
        return

def read(led_colour):
    if led_colour == "green":
        device = green_led

    elif led_colour == "red":
        device = red_led
    
    else:
        return

    return os.system("cat " + device + "/brightness")
