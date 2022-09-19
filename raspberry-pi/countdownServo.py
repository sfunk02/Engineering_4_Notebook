# type: ignore
import board
import digitalio
import pwmio
import time
from adafruit_motor import servo    #imports servo library

button = digitalio.DigitalInOut(board.GP27) #identifies button pin
button.direction = digitalio.Direction.INPUT    #identifies GP27 as input
button.pull = digitalio.Pull.DOWN       #sets button pin as a pulldown resistor

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
G = digitalio.DigitalInOut(board.GP28)
R.direction = digitalio.Direction.OUTPUT    #sets pin to output
G.direction = digitalio.Direction.OUTPUT

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)   #defines pwm output for the servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)      #defines the servo object

switchstate = False     #switchstates make it so a button doesn't spam commands
switchstate2 = False

servo1.angle = 5    #tells the servo where to start

while True:
    Abort = False
    if button.value == False and switchstate2 == True:
        switchstate2 = False
    elif button.value == True and switchstate == False and switchstate2 == False:    #if button is pressed
        switchstate = True
        for x in range(10):     #counts 10 numbers, so 0 to 9
            print (10 - x)    #reverses the order so it starts at 10
            if button.value == False and switchstate == True:       #switchstate switches once the button is released
                switchstate = False
            elif button.value == True and switchstate == False:     #Abort only happens if the button is pressed again
                    print("Abort")
                    Abort = True
                    switchstate2 = True
                    R.value = False
                    break       #breaks out of the for loop
            R.value = True      #turns red LED on
            time.sleep(.1)
            if button.value == False and switchstate == True:
                switchstate = False
            elif button.value == True and switchstate == False:
                    print("Abort")
                    Abort = True
                    switchstate2 = True
                    R.value = False
                    break
            R.value = False     #turns red LED off
            time.sleep(.9)
            if button.value == False and switchstate == True:
                switchstate = False
            elif button.value == True and switchstate == False:
                    print("Abort")
                    Abort = True
                    switchstate2 = True
                    R.value = False
                    break
        if Abort == False:      #Liftoff only prints if Abort has not been activated
            print("Liftoff")
            servo1.angle = 175      #turns servo
            while True:
                G.value = True      #turns on green LED forever