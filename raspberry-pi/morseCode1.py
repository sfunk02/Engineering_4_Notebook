# type: ignore

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