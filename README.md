# InMoov AI Hand Robotic Project

## Overview

This project involves building and programming an **InMoov robotic hand and forearm** controlled by servo motors, utilizing a **Raspberry Pi 4**. The robotic hand mimics human hand movements captured through a **camera** using **OpenCV**. This README provides an overview of the project's progress, functionality, and implementation details.

## Features

- **Servo Motor Control:** The robotic hand is powered by servo motors controlled through the PCA9685 driver.
- **Hand Tracking with OpenCV:** A camera tracks human hand movements, and the robotic hand replicates them in real-time.
- **Python-Based Control System:** The entire system is implemented in Python, leveraging libraries like OpenCV, MediaPipe, and Adafruit PCA9685.
- **Flexible and Modular Design:** The project is designed to be adaptable for future improvements, such as adding voice commands or IoT integration.

## Components

### Hardware

- **Raspberry Pi 4**: The central processing unit for controlling the robotic hand.
- **5V 30A 150W Power Supply**: Provides power to the PCA9685 driver and five servo motors, ensuring stable and sufficient current for operation.
- **PCA9685 Driver**: Controls up to 16 PWM signals for the servo motors.
- **HK-15298 Servo Motors**: Five motors to control the fingers.
- **Raspberry Pi HQ Camera**: Used to track hand movements.

### Software

- **OpenCV**: For hand tracking and gesture recognition.
- **Adafruit PCA9685 Library**: For interfacing with the servo motor driver.
- **Python**: The primary programming language for the project.

## Circuit Diagram



## How to Run

1. **Set up hardware:**
   - Connect the PCA9685 driver to the Raspberry Pi.
   - Attach the servo motors to the robotic hand.
   - Connect the camera to the Raspberry Pi.
2. **Install dependencies:**
   ```bash
   pip install opencv-python mediapipe adafruit-circuitpython-pca9685
   ```
3. **Run the script:**
   ```bash
   python hand_tracking_control.py
   ```

## Demonstration

### Images

1. **Servo Testing**:

2. **Hand Tracking**:

3. **Full System**:

### Video

[Link to Demonstration Video](https://your.video.link)

## Future Improvements

- **Haptic Feedback**: Add feedback to gloves and make it control the robotic hand
- **IoT Integration**: Control the hand remotely via the internet.
- **Voice Commands**: Integrate speech recognition for combined voice and gesture control. (Maybe even have a rock paper scissor game)

## License

This project is licensed under the MIT License. See the LICENSE file for details.




I was able to get a lot of help from the people within the discord server:
https://discord.gg/FKJ6GSEwHr