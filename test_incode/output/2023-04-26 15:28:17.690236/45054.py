#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports. """    
    while True:
        ports = os.listdir('/sys/class/net/')
        for port in ports:
            port = int(port)
            if port not in range(1,65535):
                