import time
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class ServoController:
    def __init__(self, frequency=50):
        # Create I2C bus
        self.i2c = busio.I2C(board.SCL, board.SDA)
        # Create PCA9685 object
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = frequency  # Set frequency for servo motor

    def set_servo_angle(self, channel, angle):
        servo_motor = servo.Servo(self.pca.channels[channel])
        servo_motor.angle = angle
        print("Servo => channels:", channel, "angle:", angle)

    def deinit(self):
        self.pca.deinit()
