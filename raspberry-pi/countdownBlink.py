# type: ignore
import board
import digitalio
import time

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
G = digitalio.DigitalInOut(board.GP28)
R.direction = digitalio.Direction.OUTPUT    #sets pin to output
G.direction = digitalio.Direction.OUTPUT

for x in range(10): #counts 10 numbers, so 0 to 9
    print (10 - x)    #reverses the order so it starts at 10
    R.value = True      #turns red LED on
    time.sleep(.1)
    R.value = False     #turns red LED off
    time.sleep(.9)
print("Liftoff")

while True:
    G.value = True      #turns on green LED forever