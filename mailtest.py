from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def mail():
    mail_content ='''Note:do not reply this is system generation'''
    # The mail addresses and password
    sender_address = 'pnitech20@gmail.com'
    sender_pass = '882838916388'
    receiver_address = 'rohitstar2050@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'TEST Mail from Heroku'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

while True:
    x=datetime.now()
    min=x.minute
    if min%2==0:
        # print("yes")
        mail()
        time.sleep(60)
    else:
        # print("no")


