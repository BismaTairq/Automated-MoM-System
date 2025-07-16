import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def send_email(to_emails, pdf_path):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = "Meeting Minutes"

    part = MIMEBase('application', 'octet-stream')
    with open(pdf_path, "rb") as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(pdf_path)}"')
    msg.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL, APP_PASSWORD)  
        server.send_message(msg)
        server.quit()
        print("✅ Email sent")
    except Exception as e:
        print("❌ Email failed:", str(e))