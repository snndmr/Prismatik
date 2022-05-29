import os
import re

import psutil
import serial.tools.list_ports


# To get CH340 port
def get_port():
    ports = serial.tools.list_ports.comports()
    for port, desc, _ in ports:
        if 'CH340' in desc:
            return port


# To update prismatik configuration
def update_config(port):
    with open(config_path, "r") as file:
        lines = file.readlines()

    with open(config_path, "w") as file:
        for line in lines:
            file.write(re.sub("COM.", port, line))


def restart_prismatik():
    for proc in psutil.process_iter():
        if proc.name() == 'Prismatik.exe':
            proc.kill()

    update_config(get_port())
    os.startfile(prismatik_path)


if __name__ == '__main__':
    config_path = 'C:\\Users\\{}\\Prismatik\\main.conf'.format(os.environ.get('USERNAME'))
    prismatik_path = 'C:\\Program Files\\Prismatik\\Prismatik.exe'

    restart_prismatik()
