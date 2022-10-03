# type: ignore

import board
import busio
import digitalio
import time
import adafruit_mpu6050
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.triangle import Line
from adafruit_display_shapes.triangle import Circle
import adafruit_displayio_ssd1306
import terminalio
import displayio

def triangle_area(x1, y1, x2, y2, x3, y3):  #defines a function for triangle area that takes six inputs
    total = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 #the math behind the function, using the six inputs
    return abs(total)   #returns absolute value of previous math

while True:
    try:        #tries this code, runs normally with no errors
        print("Enter the first coordinate in format x,y:")
        first = input()             #takes first input/coordinate
        first = first.split(",")    #splits input at the comma, separating into x and y
        x1 = float(first[0])    #calls on first value (x)
        y1 = float(first [1])   #calls on second value (y)
        print("Enter the second coordinate in format x,y:")
        second = input()
        second = second.split(",")
        x2 = float(second[0])
        y2 = float(second [1])
        print("Enter the third coordinate in format x,y:")
        third = input()
        third = third.split(",")
        x3 = float(third[0])
        y3 = float(third [1])

        area = triangle_area(x1, y1, x2, y2, x3, y3)    #calls on triangle area function using the recorded inputs
        print(f"The area of the triangle with vertices ({first[0]},{first[1]}), ({second[0]},{second[1]}), and ({third[0]},{third[1]}) is {area} square km.")
    except:     #if there's an error, skips to this step and restarts the while True loop
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")