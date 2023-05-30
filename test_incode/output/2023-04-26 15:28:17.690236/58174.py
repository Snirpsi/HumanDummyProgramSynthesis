#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or opens all ports. """    
    while True:
        ports = open('/dev/ttyACM0', 'r').read().splitlines()
        for port in ports:
            cmd = 'echo "{}" | sudo tee -a /etc/ttyACM0/serial.conf'.format(port)
            subprocess.call(cmd, shell=True)
