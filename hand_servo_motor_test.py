from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory()
servo_pins = [18, 19, 20, 21, 22, 23]
servos = [(pin, Servo(pin, pin_factory=factory)) for pin in servo_pins]

try:
    while True:
        for pin, servo in servos:
            print(f"Moving servo on pin {pin} to -1")
            servo.value = -1
            time.sleep(3)
            print(f"Moving servo on pin {pin} to 1")
            servo.value = 1
            time.sleep(3)
except KeyboardInterrupt:
    for pin, servo in servos:
        servo.value = None
