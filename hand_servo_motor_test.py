import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

try:
    # Set up I2C communication
    i2c = busio.I2C(SCL, SDA)

    # Set up the PCA9685 driver
    pca = PCA9685(i2c)
    pca.frequency = 50  # Standard frequency for servos

    # Function to move a servo
    def move_servo(channel, position):
        """Move servo to a specific position."""
        positions = {
            0: 0x1999,  # 0° position
            90: 0x7FFF, # 90° position
            180: 0xE665 # 180° position
        }
        servo_channel = pca.channels[channel]
        servo_channel.duty_cycle = positions[position]
        print(f"Moving servo on channel {channel} to {position}°")
        time.sleep(2)  # 2-second delay

    # List of channels for the fingers
    fingers = {
        "pinky": 0,
        "ring": 1,
        "middle": 2,
        "index": 3,
        "thumb": 4
    }

    # Move each finger through the sequence
    for finger, channel in fingers.items():
        print(f"Controlling {finger.capitalize()} finger on channel {channel}")
        move_servo(channel, 0)    # Move to 0°
        move_servo(channel, 90)   # Move to 90°
        move_servo(channel, 180)  # Move to 180°
        move_servo(channel, 90)   # Move back to 90°
        move_servo(channel, 0)    # Move back to 0°

    # Turn off all servos
    print("Turning off all servos")
    for channel in fingers.values():
        pca.channels[channel].duty_cycle = 0

except Exception as e:
    print(f"An error occurred: {e}")