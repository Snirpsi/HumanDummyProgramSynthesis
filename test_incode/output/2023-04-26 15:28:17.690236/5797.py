#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        ports = os.listdir('/sys/class/net/')
        for port in ports:
            if port.startswith('eth'):
                os.system('sudo 