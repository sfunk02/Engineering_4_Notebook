# type: ignore
import board
import digitalio
import time

MORSE_CODE = { 'A':'.-', 'B':'-...',       #dictionary that defines each letter in morse code
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}     #I had to add one so that spaces translate to slashes

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
R.direction = digitalio.Direction.OUTPUT    #sets pin to output

mod = 0.25
dot = 1*mod     #sets amount of time for each LED blink type
dash = 3*mod
tap_gap = 1*mod
letter_gap = 3*mod
word_gap = 7*mod

print("Enter message to be translated into Morse Code or type -q to quit:")
string = ""     #empty string to be used later
while True:
    message = input()
    if message == "-q":
        break   #quits the while true loop
    for letter in message.upper():  #runs through each letter in the message
        string += MORSE_CODE[letter]    #adds translation to the empty string
        string += " "   #followed by a space
    print(string)   #prints completed string
    for character in string:    #goes through each character in the message
        if character == ".":    #short blink for dot
            R.value = True
            time.sleep(dot)
            R.value = False
            time.sleep(tap_gap)
        elif character == "-":  #longer blink for dash
            R.value = True
            time.sleep(dash)
            R.value = False
            time.sleep(tap_gap)
        elif character == " ":
            time.sleep(letter_gap)
        elif character == " / ":
            time.sleep(word_gap)