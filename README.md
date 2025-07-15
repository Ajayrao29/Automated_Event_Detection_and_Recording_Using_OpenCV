🎥 Automated Event Detection and Recording using OpenCV
A smart, real-time surveillance system built using Python and OpenCV that detects human presence using a webcam, records video only when a person is detected, and sends email alerts with snapshots.

⚡ Efficient | 📷 Real-Time | 📩 Email Alerts | 💾 Optimized Storage & Power Usage

📌 Features
🎯 Real-time Human Detection using Haar Cascade Classifier
🎥 Video Recording triggered only by human presence
📨 Email Alerts with attached image snapshots
💽 Optimized Storage & Power usage
🧠 Built with Python + OpenCV
⚙️ Easily extensible to detect fire, falls, or weapons

📸 System Architecture
[Webcam Input] → [Frame Processing]
            ↓
      [Face Detection using Haar Cascade]
            ↓
┌────────────────────┬────────────────────┐
↓                        ↓
Start Recording           Stop Recording after Inactivity
   ↓                    ↓
   Save Video           Send Email Alert with Snapshot

🛠️ Technologies Used
Python – Core programming logic
OpenCV – Face/human detection, video processing
Haar Cascade – Pre-trained object detection model
smtplib + email.mime – Sending email alerts with attachments
Threading – To avoid freezing the main video feed during alerts
Jupyter Notebook – Testing & prototyping

🚀 Getting Started
✅ Prerequisites
Python3
Webcam
Gmail account for alerts

📦 Install Dependencies
Use pip to install OpenCV:
pip install opencv-python

🧠 How It Works
Captures frames using the webcam
Converts each frame to grayscale
Detects faces using Haar Cascade
Starts video recording and sends an email alert if a face is found
Stops recording when no face is detected for a period

📂 Folder
📁 Project files
├── Final.py                        # Main script
├── haarcascade_frontalface_default.xml   # Haar model (OpenCV)
├── output.mp4                     # Sample recorded video
├── person_detected_*.jpg          # Captured snapshot images
└── README.md                      # This file

📧 Email Configuration

In your Final.py, update the following values:

sender_email = "youremail@gmail.com"
receiver_email = "alertrecipient@gmail.com"
password = "your_app_password"
⚠️ Use App Passwords from Gmail (not your real password).
Ensure 2FA is enabled and "Less secure app access" is allowed or generate App Passwords.

📈 Future Enhancements
🔥 Add fire, fall, and weapon detection using deep learning (e.g., YOLOv8)
☁️ Cloud storage for video logs (Google Drive, Firebase, etc.)
📱 Mobile push notifications using Twilio or Firebase
🌙 Support for low-light conditions using IR cameras
🖥️ Add a web dashboard to view logs and live stream
