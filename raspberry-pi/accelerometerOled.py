# type: ignore
import board
import busio
import digitalio
import time
import adafruit_mpu6050
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
R.direction = digitalio.Direction.OUTPUT    #sets pin to output

initial = time.monotonic()
initial = int(initial)

while True:
    splash = displayio.Group()
    title = "ANGULAR VELOCITY"
    X = round(mpu.gyro[0], 3)
    Y = round(mpu.gyro[1], 3)
    Z = round(mpu.gyro[2], 3)
    x = f"X: {X} rad/s"
    y = f"Y: {Y} rad/s"
    z = f"Z: {Z} rad/s"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    text_area2 = label.Label(terminalio.FONT, text=x, color=0xFFFF00, x=5, y=20)
    text_area3 = label.Label(terminalio.FONT, text=y, color=0xFFFF00, x=5, y=35)
    text_area4 = label.Label(terminalio.FONT, text=z, color=0xFFFF00, x=5, y=50)
    splash.append(text_area)
    splash.append(text_area2)
    splash.append(text_area3)
    splash.append(text_area4)
    display.show(splash)
    if time.monotonic() - initial > 1:
        print(f"X Acceleration: {mpu.acceleration[0]} m/s^2")   #prints x
        print(f"Y Acceleration: {mpu.acceleration[1]} m/s^2")
        print(f"Z Acceleration: {mpu.acceleration[2]} m/s^2")
        print("")       #blank line
        initial += 1
    if mpu.acceleration[0] > 9.5 or mpu.acceleration[0] < -9.5:   #if board is tilted in x direction
        R.value = True                                              #led turns on
    elif mpu.acceleration[1] > 9.5 or mpu.acceleration[1] < -9.5:     #if board is tilted in y direction
        R.value = True
    else:
        R.value = False