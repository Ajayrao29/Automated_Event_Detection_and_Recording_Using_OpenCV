🎥 Automated Event Detection and Recording using OpenCV
A smart, real-time surveillance system built using Python and OpenCV
that detects human presence using a webcam, records video only when a person is detected,
and sends email alerts with snapshots.

⚡ Efficient | 📷 Real-Time | 📩 Email Alerts | 💾 Optimized Storage

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
┌─────────────┬─────────────┐
↓                  ↓
Start Recording       Stop Recording after Inactivity
   ↓             ↓
Save Video       Send Email Alert with Snapshot

🛠️ Technologies Used
Technology	Purpose
Python	Core programming logic
OpenCV	Face/human detection, video processing
Haar Cascade	Pre-trained object detection model
smtplib/email.mime	Sending email alerts with attachments
Threading	Background email sending
Jupyter Notebook	Testing & prototyping

🚀 Getting Started
✅ Prerequisites
Python 3.x

Webcam

Gmail account for email alerts

📦 Install Dependencies
Open terminal and run:

pip install opencv-python

🧠 How It Works
Captures frames using the webcam

Converts each frame to grayscale

Detects faces using Haar Cascade

Starts recording and sends email alert if a face is detected

Stops recording when no face is detected

📂 Folder Structure
📁 Project Root
├── Final.py → Main Python script
├── haarcascade_frontalface_default.xml → Haar model file
├── output.mp4 → Sample recorded video
├── person_detected_*.jpg → Captured snapshots
└── README.md → Project documentation

📧 Email Configuration
In Final.py, set:

sender_email = "youremail@gmail.com"
receiver_email = "receiveremail@gmail.com"
password = "your_app_password"

⚠️ Use Gmail App Passwords, not your actual Gmail password.
Enable 2FA and create an App Password in your Google account.

📈 Future Enhancements
🔥 Add fire, fall, and weapon detection using YOLO or deep learning

☁️ Cloud video storage (Google Drive, Firebase)

📱 Mobile push notifications using Twilio or Firebase

🌙 Night vision with IR camera integration

🖥️ Web dashboard for logs and live streaming
