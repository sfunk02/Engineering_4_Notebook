# type: ignore
import board
import busio
import time
import adafruit_mpu6050

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(f"X Acceleration: {mpu.acceleration[0]} m/s^2")
    print(f"Y Acceleration: {mpu.acceleration[1]} m/s^2")
    print(f"Z Acceleration: {mpu.acceleration[2]} m/s^2")
    print("")
    time.sleep(1)