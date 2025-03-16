import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # try:
        # Set up the email
    msg = MIMEMultipart()
    msg['From'] = "Joshua Anang"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach any file if provided
    # if attachment_path:
    #     with open(attachment_path, 'rb') as attachment:
    #         part = MIMEBase('application', 'octet-stream')
    #         part.set_payload(attachment.read())
    #         encoders.encode_base64(part)
    #         part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
    #         msg.attach(part)
    
    # Connect to Gmail's SMTP server and send email
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("joshuaanang783@gmail.com", os.getenv('APP_PASSWORD'))
    server.sendmail("joshuaanang783@gmail.com", receiver_email, msg.as_string())
    server.quit()
        
    print("Email sent successfully!")


send_email(
    sender_email="joshuaanang783@gmail.com",
    sender_password=os.getenv('APP_PASSWORD'),  # Use app-specific password if 2FA is enabled
    receiver_email="anangjosh8@gmail.com",
    subject="Digital HealthTech Startup - 500+ customers - US - Pre-Seed",
    body="I will be king of the pirates",
    attachment_path="None"  # Set to None if no attachment
)