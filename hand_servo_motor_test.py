import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

# Set up I2C communication
i2c = busio.I2C(SCL, SDA)

# Set up the PCA9685 driver
pca = PCA9685(i2c)
pca.frequency = 50  # Standard frequency for servos

# Control servo on channel 0
servo_channel = pca.channels[0]

# Move the servo to different positions
servo_channel.duty_cycle = 0x1999  # 0° position
time.sleep(1)
servo_channel.duty_cycle = 0x7FFF  # 90° position
time.sleep(1)
servo_channel.duty_cycle = 0xE665  # 180° position
time.sleep(1)

# Turn off the servo
servo_channel.duty_cycle = 0
