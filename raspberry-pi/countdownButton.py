# type: ignore
import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GP27) #identifies button pin
button.direction = digitalio.Direction.INPUT    #identifies GP27 as input
button.pull = digitalio.Pull.DOWN       #sets button pin as a pulldown resistor

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
G = digitalio.DigitalInOut(board.GP28)
R.direction = digitalio.Direction.OUTPUT    #sets pin to output
G.direction = digitalio.Direction.OUTPUT

i = 1

while True:
    if button.value and i == 1:    #if button is pressed
        i = 0
        for x in range(10): #counts 10 numbers, so 0 to 9
            if button.value and i == 1: #not doing anything right now
                print("Abort")
                i = 1
            elif i == 0:
                print (10 - x)    #reverses the order so it starts at 10
                R.value = True      #turns red LED on
                time.sleep(.1)
                R.value = False     #turns red LED off
                time.sleep(.9)
        print("Liftoff")

        while True:
            G.value = True      #turns on green LED forever