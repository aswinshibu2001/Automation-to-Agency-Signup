import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import config


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = config.MAIL
SENDER_PASSWORD = config.PASSWORD 

def send_email(receiver_email,subject,status,reason):

    msg=EmailMessage()
    msg["Subject"]= subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    msg.set_content(
        f"""
        Dear User,

        Congratulations! Your website has been classified as a **Digital Marketing Agency**.

        You can proceed with the next steps.
        {reason}
        Best Regards,
        Your Team
        """
    )

    with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,receiver_email,msg.as_string())

if __name__=="__main__":
    send_email(
        "masterofkings2023@gmail.com",
        "subject",
        "accepted",
        "reson for accept"
    )