# 🎯 Color-Based Object Tracking Robot (Webots Simulation)

This Webots project features a robot equipped with a camera that uses object recognition to identify and track a specific colored object (e.g., purple). The robot rotates until it sees the target object and then aligns and moves toward it.

---

## 📌 Features

- 📷 **Camera-based Object Recognition**
- 🎯 **Target Color Tracking (e.g., purple-toned)**
- 🔁 **Rotation to scan environment if target is not visible**
- ➡️ **Alignment and approach logic based on object position**
- 🧠 **Dynamic speed adjustments for turning or forward movement**

---

## 🚀 Technologies Used

- [Webots](https://cyberbotics.com/) Simulator
- Python Controller (Webots API)
- Camera + Object Recognition Sensors

---

## 🧠 How It Works

### 🔍 Object Recognition and Target Detection

- The robot uses Webots' `recognitionEnable()` function to get a list of recognized objects.
- Each object provides `colors[]`, from which only RGB components are compared with a `TARGET_COLOR`.
- A color threshold allows for slight variation in target color detection.

### 🤖 Movement Strategy

- **No object detected**: Rotate in place to scan surroundings.
- **Object detected but off-center**: Rotate toward the object to align.
- **Object centered**: Move forward.
- **Object very close**: Stop movement.

---

## 🛠️ Customization

- 🎨 **Change Target Color**:
  ```python
  TARGET_COLOR = [0.8, 0.5, 0.5]  # Adjust this for your desired color


---

## 👩‍💻 Developers Information

Developed by **[Sheema Firdous](https://www.linkedin.com/in/sheema-firdous-67b9b8181/)**  
as part of the **Cognitive Systems and Robotics** module assessment  at **[Sheffield Hallam University](https://www.shu.ac.uk/)**

Supervised by [Dr. Samuele Vinanzi](https://www.linkedin.com/in/samuelevinanzi/)

This project demonstrates the practical application of VISION in Cognitive and Autonomous robotics using Webots and Python.
