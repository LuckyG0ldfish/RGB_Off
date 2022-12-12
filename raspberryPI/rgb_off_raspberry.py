# Import the necessary libraries
import time
import RPi.GPIO as GPIO

# Set the mode of the GPIO pins
GPIO.setmode(GPIO.BCM)

# Set the pins that will be used to control the RGB lights
red_pin = 17
green_pin = 18
blue_pin = 27

# Set the pins as output pins
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Turn off the RGB lights
GPIO.output(red_pin, False)
GPIO.output(green_pin, False)
GPIO.output(blue_pin, False)

# Clean up the GPIO pins
GPIO.cleanup()
