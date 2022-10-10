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
import math

points = [['-50,-17','-57,12','-22,-7'],['28,-14','60,-7','54,18'],['45,30','51,-1','18,6'],['5,5','19,15','22,10']]

def triangle_area(x1, y1, x2, y2, x3, y3):  #defines a function for triangle area that takes six inputs
    total = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 #the math behind the function, using the six inputs
    return abs(total)   #returns absolute value of previous math

def centroid_distance(x1, y1, x2, y2, x3, y3):
    center = [((x1 + x2 + x3) / 3),((y1 + y2 +y3) / 3)]
    center.split(",")
    return math.sqrt((center[0] * center[0]) + (center[1] * center[1]))

displayio.release_displays()

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)       #sets up i2c connection

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)   #sets up oled screen with i2c communication
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

Afirst = points[0][0]             #takes first input/coordinate
Afirst = Afirst.split(",")    #splits input at the comma, separating into x and y
Ax1 = int(Afirst[0])    #calls on first value (x)
Ay1 = int(Afirst [1])   #calls on second value (y)
Asecond = points[0][1]
Asecond = Asecond.split(",")
Ax2 = int(Asecond[0])
Ay2 = int(Asecond [1])
Athird = points[0][2]
Athird = Athird.split(",")
Ax3 = int(Athird[0])
Ay3 = int(Athird [1])

Bfirst = points[1][0]             
Bfirst = Bfirst.split(",")   
Bx1 = int(Bfirst[0])    
By1 = int(Bfirst [1])  
Bsecond = points[1][1]
Bsecond = Bsecond.split(",")
Bx2 = int(Bsecond[0])
By2 = int(Bsecond [1])
Bthird = points[1][2]
Bthird = Bthird.split(",")
Bx3 = int(Bthird[0])
By3 = int(Bthird [1])

Cfirst = points[2][0]             
Cfirst = Cfirst.split(",")    
Cx1 = int(Cfirst[0])    
Cy1 = int(Cfirst [1])   
Csecond = points[2][1]
Csecond = Csecond.split(",")
Cx2 = int(Csecond[0])
Cy2 = int(Csecond [1])
Cthird = points[2][2]
Cthird = Cthird.split(",")
Cx3 = int(Cthird[0])
Cy3 = int(Cthird [1])

areaA = triangle_area(Ax1, Ay1, Ax2, Ay2, Ax3, Ay3)
distanceA = centroid_distance(Ax1, Ay1, Ax2, Ay2, Ax3, Ay3)    #calls on triangle area function using the recorded inputs
areaB = triangle_area(Bx1, By1, Bx2, By2, Bx3, By3)
distanceB = centroid_distance(Bx1, By1, Bx2, By2, Bx3, By3)
areaC = triangle_area(Cx1, Cy1, Cx2, Cy2, Cx3, Cy3)
distanceC = centroid_distance(Cx1, Cy1, Cx2, Cy2, Cx3, Cy3)

splash = displayio.Group()
print(f"{Afirst[0]},{Afirst[1]}), ({Asecond[0]},{Asecond[1]}), ({Athird[0]},{Athird[1]})")
title = f"{areaA}km^2"       #shows area of triangle at the top
triangle = Triangle(Ax1 + 64, 32 - Ay1, Ax2 + 64, 32 - Ay2, Ax3 + 64, 32 - Ay3, outline=0xFFFF00) #triangle, based on input coordinates
splash.append(triangle)

text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
hline = Line(0,32,128,32, color=0xFFFF00)   #horizontal line
vline = Line(64,0,64,64, color=0xFFFF00)    #vertical line
circle = Circle(64, 32, 2, outline=0xFFFF00)    #circle in the center
splash.append(circle)
splash.append(hline)
splash.append(vline)
splash.append(text_area)
display.show(splash)

print(f"{Bfirst[0]},{Bfirst[1]}), ({Bsecond[0]},{Bsecond[1]}), ({Bthird[0]},{Bthird[1]})")
title = f"{areaB}km^2"       #shows area of triangle at the top
triangle = Triangle(Bx1 + 64, 32 - By1, Bx2 + 64, 32 - By2, Bx3 + 64, 32 - By3, outline=0xFFFF00) #triangle, based on input coordinates
splash.append(triangle)
display.show(splash)