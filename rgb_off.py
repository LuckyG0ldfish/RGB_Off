# Import the necessary libraries
import time
import win32api

# Set the pins that will be used to control the RGB lights
red_pin = 1
green_pin = 2
blue_pin = 3

# Turn off the RGB lights
win32api.SetGpio(red_pin, False)
win32api.SetGpio(green_pin, False)
win32api.SetGpio(blue_pin, False)
