#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports. """    
    while True:
        ports = os.listdir('.')
        for port in ports:
            port = int(port)
            if port > 0 and port < 65535:
                