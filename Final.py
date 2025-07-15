import cv2
from datetime import datetime, timedelta
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import threading

# === Email sending function ===
def send_email(image_path):
    sender_email = "ajayrao1294@gmail.com"
    receiver_email = "ajayraolingampalli119@gmail.com"
    password = "uzuk wpuy aels wyeu"  # App Password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Alert: Person Detected!"

    msg.attach(MIMEText("A person has been detected. Please see the attached image.", 'plain'))

    with open(image_path, 'rb') as fp:
        img_data = fp.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# === Load Haarcascade for face detection ===
person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_writer = None
person_detected = False
last_email_time = datetime.now() - timedelta(minutes=10)
email_interval = timedelta(minutes=10)

# === Save frame and send alert ===
def send_alert(frame):
    current_time = datetime.now()
    exact_time = current_time.strftime('%Y-%b-%d-%H-%M-%S-%f')
    image_path = "person_detected_" + exact_time + ".jpg"
    cv2.imwrite(image_path, frame)
    threading.Thread(target=send_email, args=(image_path,)).start()

# === Start video recording ===
def start_recording(frame):
    global video_writer
    if video_writer is None:
        height, width, _ = frame.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter("output.mp4", fourcc, 5.0, (width, height))

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    video_writer.write(frame)

# === Process each frame ===
def process_frame(frame):
    global person_detected, last_email_time
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    persons = person_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(persons) > 0:
        current_time = datetime.now()
        if (current_time - last_email_time) >= email_interval:
            last_email_time = current_time
            send_alert(frame)
        start_recording(frame)
        person_detected = True
    else:
        person_detected = False

# === Set correct camera index and backend ===
camera_index = 2  # Change this to 0 or 1 if needed
video = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)  # Use CAP_DSHOW for Windows

if not video.isOpened():
    print("❌ Webcam could not be opened. Please check your camera or drivers.")
    exit()

print("✅ Webcam started. Press 'q' to quit.")

# === Main loop ===
while True:
    ret, frame = video.read()
    if not ret or frame is None:
        print("❌ Failed to grab frame.")
        continue

    process_frame(frame)

    cv2.imshow("Home Surveillance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === Cleanup ===
video.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
