# 🧠 E-Brain Core IA  
**Electronic Brain Connect Core with Integrated AI**

---

## 📌 Overview
**E-Brain Core IA** is a **hybrid cognitive system** designed as an *electronic brain* to bridge humans and machines.  
It combines **real-time sensor and actuator control** with a **lightweight AI engine** (TinyLlama or similar) for analysis, adaptive decision-making, and memory simulation.  

Inspired by the concept of a *positronic brain*, E-Brain Core IA aims to become the **core prosthetic brain** for assistive robotics, prosthetics, and wearable devices.

---

## 🚀 Vision
To create an **international open-source cognitive platform** that empowers:
- **Medical rehabilitation** → control of prosthetics and exoskeletons.  
- **Assistive technologies** → real-time monitoring and safety systems.  
- **Human–machine interfaces** → intuitive connection between humans and digital/robotic systems.  
- **Cognitive and emotional support** → hybrid AI capable of analyzing human input and providing guidance.  

---

## 🧩 System Architecture
E-Brain Core IA is structured as a **modular brain-inspired system**:

1. **Perception** → sensors (EMG, IMU, audio, proximity, vision, temperature).  
2. **Processing** → feature extraction, signal normalization, memory (short/long-term).  
3. **Decision** → classifiers, adaptive thresholds, AI-based reasoning.  
4. **Actuation** → motors, prosthetics, exoskeletons, or external devices.  
5. **Feedback** → haptic, visual, or auditory responses to the user.  

---

## 🛠️ MVP – Minimum Viable Prototype
- **Hardware**:  
  - Arduino UNO/Mega (or ESP32)  
  - 2–4 EMG channels (MyoWare or similar)  
  - 1–3 servo motors (basic prosthetic gripper)  
  - Vibromotors for haptic feedback  

- **Software**:  
  - Real-time signal acquisition (1 kHz sampling)  
  - Filtering, rectification, and RMS calculation  
  - Simple classifier (threshold + LDA) for open/close gesture  
  - PWM motor control + safety watchdog  
  - Feedback vibration when force threshold is exceeded  

---

## 📜 Roadmap
- **Stage 1**: Sensor & motor simulation (reflex loops).  
- **Stage 2**: Prosthetic prototype (hand/gripper).  
- **Stage 3**: Adaptive memory and decision-making.  
- **Stage 4**: Integration of **TinyLlama** (lightweight LLM) for real-time analysis.  
- **Stage 5**: Wearable form (portable cognitive brain for assistive devices).

- Current status: Stage 3 - 16/08/2025

---

## 🔐 License
This project is licensed under the **MPL 2.0** license.  
- Open source usage is free as long as modifications to existing source files remain open.  
- For **commercial/proprietary usage** without code disclosure, please contact the author for a **commercial license option**.  

---

## 🌍 International Scope
All documentation is provided in **English** to ensure accessibility for researchers, companies, and collaborators worldwide.  

---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repository  
- Create your feature branch (`git checkout -b feature/my-feature`)  
- Commit changes (`git commit -m 'Add new feature'`)  
- Push to the branch (`git push origin feature/my-feature`)  
- Open a Pull Request  

---

## 📧 Contact
Author: **David Arriaga**  
Project: **E-Brain Core IA**  
Email: ebraincoreia@gmail.com
Purpose: *Building the next-generation electronic prosthetic brain with IA*  

