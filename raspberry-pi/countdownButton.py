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

switchstate = False

while True:
    Abort = False
    if button.value == True and switchstate == False:    #if button is pressed
        switchstate = True
        for x in range(10):     #counts 10 numbers, so 0 to 9
            print (10 - x)    #reverses the order so it starts at 10
            if button.value == False and switchstate == True:
                switchstate = False
            elif button.value == True and switchstate == False:
                    print("Abort")
                    Abort = True
                    break
            R.value = True      #turns red LED on
            time.sleep(.1)
            if button.value == False and switchstate == True:
                switchstate = False
            elif button.value == True and switchstate == False:
                    print("Abort")
                    Abort = True
                    break
            R.value = False     #turns red LED off
            time.sleep(.9)
            if button.value == False and switchstate == True:
                switchstate = False
            elif button.value == True and switchstate == False:
                    print("Abort")
                    Abort = True
                    break
        if Abort == False:
            print("Liftoff")
            while True:
                G.value = True      #turns on green LED forever