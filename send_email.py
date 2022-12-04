import smtplib, os
from email.message import EmailMessage

SENDER = "xfarce1@gmail.com"
RECEIVER = "xfarce1@gmail.com"
PASSWORD = os.getenv("PASSWORD")

def send_email(message):
    email_message = EmailMessage()
    email_message["Subject"] = "New Event Updated!"
    email_message.set_content("Hey, we have a new event captured!" + "\n"*2 + message)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()