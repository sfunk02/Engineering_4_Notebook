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
import time
import math

points = [[-2,-30,-19,-8,-44,-18],[7,-14,60,-7,33,-6],[5,5,-8,9,0,-6],[63,30,60,19,29,16]]  #[x1,y1,x2,y2,x3,y3]

def triangle_area(x1, y1, x2, y2, x3, y3):  #defines a function for triangle area that takes six inputs
    total = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 #the math behind the function, using the six inputs
    return abs(total)   #returns absolute value of previous math

def centroid_distance(x1, y1, x2, y2, x3, y3):  #function to determine centroid distance from the origin
    centerx = ((x1 + x2 + x3) / 3)
    centery = ((y1 + y2 + y3) / 3)
    return math.sqrt((centerx * centerx) + (centery * centery))

displayio.release_displays()

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)       #sets up i2c connection

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)   #sets up oled screen with i2c communication
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

i = 0
best = points[0]

while True:
    if i == 4:  #(after all points have been used)
        break   #ends loop
    else:
        area = triangle_area(points[i][0], points[i][1], points[i][2], points[i][3], points[i][4], points[i][5])
        distance = centroid_distance(points[i][0], points[i][1], points[i][2], points[i][3], points[i][4], points[i][5])
        print((points[i]))
        print(f"area={area}, distance={distance}")
        splash = displayio.Group()
        title = f"{area}km^2"       #shows area of triangle at the top
        triangle = Triangle(points[i][0] + 64, 32 - points[i][1], points[i][2] + 64, 32 - points[i][3], points[i][4] + 64, 32 - points[i][5], outline=0xFFFF00)
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
        hline = Line(0,32,128,32, color=0xFFFF00)   #horizontal line
        vline = Line(64,0,64,64, color=0xFFFF00)    #vertical line
        circle = Circle(64, 32, 2, outline=0xFFFF00)    #circle in the center
        splash.append(triangle)
        splash.append(circle)
        splash.append(hline)
        splash.append(vline)
        splash.append(text_area)
        display.show(splash)
        if area > 100 and distance < centroid_distance(best[0],best[1],best[2],best[3],best[4],best[5]):    
            best = points[i]    #sets current triangle to "best" if it meets the requirements
        time.sleep(1)
        i += 1  #cycles to the next triangle
print(f"The closest suitable landing area has vertices ({best[0]},{best[1]}), ({best[2]},{best[3]}), and ({best[4]},{best[5]}). The area is {triangle_area(best[0],best[1],best[2],best[3],best[4],best[5])} km^2 and the centroid is {centroid_distance(best[0],best[1],best[2],best[3],best[4],best[5])} km away from base.")