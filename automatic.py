from gpiozero import Motor
from gpiozero import DistanceSensor
import time

# Define motors
left_motor = Motor(forward=18, backward=23)
right_motor = Motor(forward=24, backward=25)

# Define ultrasonic sensors
front_sensor = DistanceSensor(echo=19, trigger=26)
back_sensor = DistanceSensor(echo=21, trigger=20)

def forward():
    left_motor.forward()
    right_motor.forward()

def stop():
    left_motor.stop()
    right_motor.stop()

def avoid_obstacle():
    forward()
    while True:
        # Check front sensor
        if front_sensor.distance < 0.3:
            # Obstacle in front, turn right
            left_motor.forward()
            right_motor.backward()
            time.sleep(1)  # Turn right for 1 second
        else:
            # No obstacle in front, continue forward
            forward()
        
        time.sleep(1)  # Continue forward for 1 second

        # Stop
        stop()
        time.sleep(0.5)  # Stop for 0.5 seconds

        # Check back sensor
        if back_sensor.distance < 0.3:
            # Obstacle behind, turn left
            left_motor.backward()
            right_motor.forward()
            time.sleep(1)  # Turn left for 1 second
        else:
            # No obstacle behind, continue forward
            forward()
        
        time.sleep(1)  # Continue forward for 1 second

        # Stop
        stop()
        time.sleep(0.5)  # Stop for 0.5 seconds

try:
    while True:
        avoid_obstacle()
except KeyboardInterrupt:
    stop()
