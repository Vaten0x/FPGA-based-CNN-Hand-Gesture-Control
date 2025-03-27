# 🤖 InMoov Hand Gesture Recognition with FPGA Acceleration

A personal hardware-software project to control an InMoov robotic hand using real-time hand gesture recognition powered by a Convolutional Neural Network (CNN) and FPGA-based acceleration. The goal is to transition from software inference to a fully hardware-accelerated AI pipeline on the DE1-SoC board.

---

## 📌 Project Goal

Use a Pi Camera to capture hand gestures, recognize them with a trained CNN, run inference on the DE1-SoC ARM processor, and eventually accelerate the CNN on the FPGA using Verilog or HLS. The result controls a robotic InMoov hand in real time.

---

## 📁 Branching Structure

Each task is being developed in its own branch:
- `task-2`: Image data collection
- `task-3`: CNN model training
- `task-4`: TFLite model conversion
- `task-5`: Inference on ARM (DE1-SoC)
- `task-6`: FPGA control via ARM output
- `task-7`: First CNN layer in hardware
- `task-8`: Full CNN in hardware (Verilog/HLS)

The `main` branch will always reflect the **most up-to-date merged progress** from all task branches.

---

## ✅ Project Checklist

### 👋 Hardware Setup
- [✅] **Task 1 – Create the robot arm based on InMoov hand and forearm Open source site**  
  Built and tested robotic hand with servo motors. Control currently works via Python script and PWM.

---

### 📸 Software Tasks
- [ ] **Task 2 – Capture gesture images with PiCam (for initial testing)**  
  Use OpenCV on Raspberry Pi to collect training images for different hand gestures. Store in class-labeled folders.

- [ ] **Task 3 – Train CNN using Keras + TensorFlow**  
  Train a CNN model to recognize the gestures using your custom dataset. Save model as `.h5` or `.pb`.

- [ ] **Task 4 – Convert model to TFLite**  
  Optimize trained model using TensorFlow Lite for embedded inference. Output `.tflite` file for deployment.

- [ ] **Task 5 – Run model on Raspberry Pi and get working predictions**  
  Use TFLite interpreter to load the model and run real-time inference on the Raspberry Pi.

- [ ] **Task 6 – Run model on ARM (DE1-SoC) with USB web camera and get working predictions**  
  Use TFLite interpreter to load the model and run real-time inference on the ARM Cortex-A9 Linux system inside DE1-SoC.

- [ ] **Task 7 – Send prediction result to FPGA and control robotic hand**  
  Use memory-mapped I/O to communicate gesture output from ARM to FPGA. FPGA uses Verilog to read input and generate appropriate PWM signals to move the robot hand.

---

### 🔧 FPGA Hardware Acceleration
- [ ] **Task 8 – Replace first CNN layer (convolution) with FPGA block**  
  Implement the first convolutional layer in hardware using either Intel HLS or manual Verilog design. Validate outputs against software.

- [ ] **Task 9 – Build full CNN in Verilog or HLS**  
  Fully port CNN inference pipeline to FPGA logic. Accept raw image input and output predicted gesture class from hardware only.

---

## 📦 Tools & Technologies

- Raspberry Pi + Pi Camera
- TensorFlow / Keras / TensorFlow Lite
- Python + OpenCV
- Intel DE1-SoC Board (Cyclone V + ARM Cortex-A9)
- Verilog / SystemVerilog (Quartus Prime)
- Intel HLS Compiler (optional)
- mmap / AXI bridge for ARM–FPGA communication

---

## 📷 Demo (Coming Soon)
- Real-time gesture detection video
- Robot hand mirroring gestures

---

## 📂 Branches Progress Overview

| Task | Branch | Description |
|------|--------|-------------|
| Task 2 | `task-2` | Image collection via PiCam |
| Task 3 | `task-3` | CNN model training |
| Task 4 | `task-4` | TFLite model conversion |
| Task 5 | `task-5` | TFLite inference on ARM |
| Task 6 | `task-6` | FPGA control via ARM result |
| Task 7 | `task-7` | CNN layer in FPGA |
| Task 8 | `task-8` | Full CNN in hardware |

---

## 🚀 Author

Jason Lee – Computer Engineering @ UBC  
Check out my progress and updates on each branch!
