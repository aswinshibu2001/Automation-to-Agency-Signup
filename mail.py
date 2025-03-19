import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import config


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = config.MAIL
SENDER_PASSWORD = config.PASSWORD 
subject="CookieYes Consent Status"

def send_email(receiver_email,url,status):

    msg=EmailMessage()
    msg["Subject"]= subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    if status=='accepted':

        msg.set_content(
            f"""
            Dear User,

            Congratulations! Your website {url} has been successfully registered with CookieYes.

            You can proceed with the next steps.
            
            Best Regards,
            CookieYes team
            """
        )
    else:
        msg.set_content(
            f"""
            Dear User,

            Unfortunately, Your website {url} has failed to meet the criteria to get registered with CookieYes.

            If you have any queries please feel free to contact us.
            
            Best Regards,
            CookieYes team
            """
        )
    try:
        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,receiver_email,msg.as_string())
        print("mail sent successfully")
    except:
        print("mail not sent error ")

    

# if __name__=="__main__":
#     send_email(
#         "masterofkings2023@gmail.com",
#         "subject",
#         "accepted",
#         "reson for accept"
#     )