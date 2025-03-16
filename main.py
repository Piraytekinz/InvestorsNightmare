import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()



body = """
Hi company_name,

My name is Joshua Anang and I'm the Founder and CEO of ChatDoc. 

We're building an AI health assistant which provides an option for United States citizens facing challenges with accessing quality and affordable healthcare.

Here's our progress so far:
- Working product has acquired over 500 users.
- Problem/solution validated through customer interviews.
- CEO has 4 years of experience with machine learning and AI.

Market size: $884.9bn

We're raising a $500K Pre-Seed round to get $30M ARR in 3 years. Would you be open to a 30 minute call next week?

Best regards,
Joshua Anang,
Founder/CEO at ChatDoc.
"""









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
    # with smtplib.SMTP('smtp.gmail.com', 465) as server:
    #     server.starttls()  # Start TLS for security
    #     server.login(sender_email, sender_password)  # Login to your email account
    #     text = msg.as_string()  # Convert the message to a string
    #     server.sendmail(sender_email, receiver_email, text)  # Send the email
        
    print("Email sent successfully!")

    # except Exception as e:
    #     print(f"Failed to send email: {e}")

# Usage

with open('txt.txt', 'r') as f:
    data = f.readlines()



links = data[0].split(' ')
names = data[1].split(',')
print(links.index('http://firstround.com/'))
n = 0
for link in links[77:]:
    og = link
    if 'www' not in link:
        n+=1
        
        if link.startswith('https://'):
            link = link.replace('https://', 'info@')
        else:
            link = link.replace('http://', 'info@')
    else:
        if link.startswith('https://www.'):
            link = link.replace('https://www.', 'info@')
        else:
            link = link.replace('http://www.', 'info@')
    
    if link != -1:
        link = link[:link.find('/')]

    company = names[links.index(og)].strip()
    print(link, names[links.index(og)])
    print(links.index(og))


    body = body.replace('company_name', company)

    
    
    

    send_email(
        sender_email="joshuaanang783@gmail.com",
        sender_password=os.getenv('APP_PASSWORD'),  # Use app-specific password if 2FA is enabled
        receiver_email="anangjosh8@gmail.com",
        subject="Digital HealthTech Startup - 500+ customers - US - Pre-Seed",
        body=body,
        attachment_path="None"  # Set to None if no attachment
    )

    break
