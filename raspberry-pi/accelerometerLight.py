# type: ignore
import board
import busio
import digitalio
import time
import adafruit_mpu6050

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

R = digitalio.DigitalInOut(board.GP1)   #identifies pin on the pico that will power the LED
R.direction = digitalio.Direction.OUTPUT    #sets pin to output

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    if mpu.acceleration[0] > 9.5 or mpu.acceleration[0] < -9.5:   #if board is tilted in x direction
        R.value = True                                              #led turns on
    elif mpu.acceleration[1] > 9.5 or mpu.acceleration[1] < -9.5:     #if board is tilted in y direction
        R.value = True
    else:
        R.value = False