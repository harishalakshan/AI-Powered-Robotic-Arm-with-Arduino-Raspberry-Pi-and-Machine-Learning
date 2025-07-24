 🤖 Advanced Robotic Arm System with Machine Learning, OpenCV, Flask, MQTT & React Dashboard

A complete Raspberry Pi + Arduino + ML powered robotic arm project with computer vision, reinforcement learning, OTA update capabilities, and a real-time web dashboard. Built for research, smart manufacturing, and educational automation.

📌 Features

- 🎯 Arduino Servo Control with Ultrasonic Sensor (Obstacle Sensing & Arm Movement)
- 📷 Object Detection with OpenCV via Raspberry Pi Camera
- 🧠 Neural Network-based prediction for angle adjustments
- 🔁 Reinforcement Learning Engine (reward-based dynamic behavior)
- 🌐 React + Flask Dashboard for real-time web control
- 📶 OTA Updates using MQTT / HTTP commands
- 🔄 Modular Architecture for easy scaling and upgrades

🧠 System Architecture

mermaid
graph TD
    A[User Interaction - React Web App] --> B[Flask Backend - Raspberry Pi]
    B --> C[Camera Input - OpenCV]
    B --> D[Machine Learning Model]
    D --> E[Prediction Engine]
    E --> F[Arduino Control via Serial]
    F --> G[Servo Motor & Ultrasonic Sensors]
    B --> H[MQTT Handler for OTA Updates]
    H --> D

📦 Tech Stack

| Layer            | Technology                          |
| ---------------- | ----------------------------------- |
| Hardware Control | Arduino Nano/Uno, Servo, Ultrasonic |
| Computer Vision  | OpenCV (Python)                     |
| Backend          | Flask (Python)                      |
| ML Engine        | TensorFlow / Keras Neural Net       |
| OTA & Messaging  | MQTT / HTTP                         |
| Frontend         | React.js                            |
| Interface Comm   | Serial (USB / UART)                 |

📁 Folder Structure

Advanced_Robotic_Arm_ML/
├── arduino/
│   └── robotic_arm_control.ino
├── backend/
│   ├── app.py
│   ├── object_detection.py
│   └── ml_model/
│       ├── model.py
│       └── training_script.py
├── ota/
│   └── mqtt_updater.py
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── components/
│   └── public/
└── README.md

🛠️ Hardware Required

* 1 × Arduino Uno / Nano
* 1 × Raspberry Pi (3 or 4)
* 3 × Servo Motors (SG90 / MG996R)
* 1 × Ultrasonic Sensor (HC-SR04)
* 1 × Raspberry Pi Camera
* Jumper Wires, Breadboard, Power Supply

🚀 Getting Started

1. Flash Arduino Code

Upload `arduino/robotic_arm_control.ino` using the Arduino IDE.

2. Install Backend Dependencies

bash
cd backend/
pip install -r requirements.txt

> Requirements: Flask, OpenCV, TensorFlow, paho-mqtt

3. Start Flask + Camera Processing

bash
python app.py

4. Launch React Frontend

bash
cd frontend/
npm install
npm start

5. Start OTA MQTT Listener

bash
cd ota/
python mqtt_updater.py

🤖 Train Your Own Neural Model

bash
cd backend/ml_model/
python training_script.py

* Input: Angle & Sensor Distance
* Output: Predicted Servo Positions
* Modify `model.py` for architecture changes
* Save to `saved_model/` directory

🔁 OTA Update Example (via MQTT)

bash
mosquitto_pub -h broker_ip -t robotic_arm/update -m "trigger_model_update"

Or trigger via HTTP from React Dashboard using:

javascript
fetch('http://localhost:5000/update_model')

🖥 Web Dashboard Features

* 🔘 Real-time servo control
* 🎥 Live camera feed (base64 stream)
* 📈 Sensor data (distance, angles)
* 🔁 Model trigger/update
* 🧠 Learning feedback (future)

🚀 Upgrade Possibilities

* 🧠 Add Reinforcement Learning reward loop (robot learns over time)
* 🔬 Integrate YOLOv5 / SSD object detection
* 🌐 Deploy dashboard on Heroku / Vercel
* 📲 Add mobile control interface (React Native)
* 🔐 Add user authentication & logging

📚 References

* [OpenCV Python Docs](https://docs.opencv.org/)
* [TensorFlow Documentation](https://www.tensorflow.org/)
* [MQTT Protocol](https://mqtt.org/)
* [Arduino Serial Communication](https://www.arduino.cc/en/Reference/Serial)

👨‍💻 Author & Credits

Built with 💡 and 💻 by [L.P. Harisha Lakshan Warnakulasuriya](https://newsletter.harishacrypto.xyz)

📬 For questions, projects, or consulting:
[unicornprofessionalbay@gmail.com](mailto:unicornprofessionalbay@gmail.com)**

📝 License

This project is licensed under the MIT License. Use freely for educational and research purposes.


