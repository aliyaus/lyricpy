import RPi.GPIO as GPIO 

"""
This block of code initializes the GPIO pin for the button and sets up its behavior.

On the Raspberry Pi: 
1. connect one of the button pins to the GPIO pin 16.
2. connect the other button pin to a GROUND pin

BUTTON_PIN = 16: 
  This specifies the GPIO pin to which the button is connected on the Raspberry Pi.  

GPIO.setmode(GPIO.BCM): 
  This sets the pin numbering system to the Broadcom SOC channel numbering system. 

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP): 
  This sets up the button pin as an input pin and enables an internal pull-up resistor. The default state is HIGH when the button is not pressed. When the button is pressed, the state changes to LOW as the button is connected to the ground.

prev_button_state = GPIO.input(BUTTON_PIN): 
  This reads the initial state of the button (which will be HIGH if the button is not being pressed, because of the pull-up resistor).
"""
def button_setup():
    BUTTON_PIN = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    prev_button_state = GPIO.input(BUTTON_PIN)
    return BUTTON_PIN, prev_button_state