🎥 Automated Event Detection and Recording using OpenCV<br/>
A smart, real-time surveillance system built using Python and OpenCV<br/>
that detects human presence using a webcam, records video only when a person is detected,<br/>
and sends email alerts with snapshots.<br/>

⚡ Efficient | 📷 Real-Time | 📩 Email Alerts | 💾 Optimized Storage<br/>

<br/>

📌 Features<br/>

🎯 Real-time Human Detection using Haar Cascade Classifier<br/>
🎥 Video Recording triggered only by human presence<br/>
📨 Email Alerts with attached image snapshots<br/>
💽 Optimized Storage & Power usage<br/>
🧠 Built with Python + OpenCV<br/>
⚙️ Easily extensible to detect fire, falls, or weapons<br/>

<br/>

📸 System Architecture<br/>

[Webcam Input] → [Frame Processing]<br/>
        ↓<br/>
[Face Detection using Haar Cascade]<br/>
        ↓<br/>
┌─────────────┬─────────────┐<br/>
↓                  ↓<br/>
Start Recording       Stop Recording after Inactivity<br/>
   ↓             ↓<br/>
Save Video       Send Email Alert with Snapshot<br/>

<br/>

🛠️ Technologies Used<br/>
| Technology | Purpose |<br/>
|--------------------|----------------------------------------|<br/>
| Python | Core programming logic |<br/>
| OpenCV | Face/human detection, video processing |<br/>
| Haar Cascade | Pre-trained object detection model |<br/>
| smtplib/email.mime | Sending email alerts with attachments |<br/>
| Threading | Background email sending |<br/>
| Jupyter Notebook | Testing & prototyping |<br/>

<br/>

✅ Prerequisites<br/>
Python 3.x<br/>
Webcam<br/>
Gmail account for email alerts<br/>

📦 Install Dependencies<br/>
Open terminal and run:<br/>
pip install opencv-python<br/>

<br/>

🧠 How It Works<br/>
Captures frames using the webcam<br/>
Converts each frame to grayscale<br/>
Detects faces using Haar Cascade<br/>
Starts recording and sends email alert if a face is detected<br/>
Stops recording when no face is detected<br/>
<br/>


📁 Project Files<br/>
├── Final.py → Main Python script<br/>
├── haarcascade_frontalface_default.xml → Haar model file<br/>
├── output.mp4 → Sample recorded video<br/>
├── person_detected_*.jpg → Captured snapshots<br/>
└── README.md → Project documentation<br/>

<br/>

📧 Email Configuration<br/>

In Final.py, set:<br/>
sender_email = "youremail@gmail.com"<br/>
receiver_email = "receiveremail@gmail.com"<br/>
password = "your_app_password"<br/>

⚠️ Use Gmail App Passwords, not your actual Gmail password.<br/>
Enable 2FA and create an App Password in your Google account.<br/>

<br/>

📈 Future Enhancements<br/>
🔥 Add fire, fall, and weapon detection using YOLO or deep learning<br/>
☁️ Cloud video storage (Google Drive, Firebase)<br/>
📱 Mobile push notifications using Twilio or Firebase<br/>
🌙 Night vision with IR camera integration<br/>
🖥️ Web dashboard for logs and live streaming<br/>

---<br/>
