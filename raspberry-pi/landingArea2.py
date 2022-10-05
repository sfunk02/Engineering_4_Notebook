# type: ignore
import board
import busio
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import adafruit_displayio_ssd1306
import terminalio
import displayio

def triangle_area(x1, y1, x2, y2, x3, y3):  #defines a function for triangle area that takes six inputs
    total = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 #the math behind the function, using the six inputs
    return abs(total)   #returns absolute value of previous math

displayio.release_displays()

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)       #sets up i2c connection

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)   #sets up oled screen with i2c communication
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

while True:
    try:        #tries this code, runs normally with no errors
        print("Enter the first coordinate in format x,y:")
        first = input()             #takes first input/coordinate
        first = first.split(",")    #splits input at the comma, separating into x and y
        x1 = int(first[0])    #calls on first value (x)
        y1 = int(first [1])   #calls on second value (y)
        print("Enter the second coordinate in format x,y:")
        second = input()
        second = second.split(",")
        x2 = int(second[0])
        y2 = int(second [1])
        print("Enter the third coordinate in format x,y:")
        third = input()
        third = third.split(",")
        x3 = int(third[0])
        y3 = int(third [1])

        area = triangle_area(x1, y1, x2, y2, x3, y3)    #calls on triangle area function using the recorded inputs
        print(f"The area of the triangle with vertices ({first[0]},{first[1]}), ({second[0]},{second[1]}), and ({third[0]},{third[1]}) is {area} square km.")
        splash = displayio.Group()
        title = f"{area}km^2"       #shows area of triangle at the top
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
        hline = Line(0,32,128,32, color=0xFFFF00)   #horizontal line
        vline = Line(64,0,64,64, color=0xFFFF00)    #vertical line
        circle = Circle(64, 32, 2, outline=0xFFFF00)    #circle in the center
        triangle = Triangle(x1 + 64, 32 - y1, x2 + 64, 32 - y2, x3 + 64, 32 - y3, outline=0xFFFF00) #triangle, based on input coordinates
        splash.append(triangle)
        splash.append(circle)
        splash.append(hline)
        splash.append(vline)
        splash.append(text_area)
        display.show(splash)
    except:     #if there's an error, skips to this step and restarts the while True loop
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")