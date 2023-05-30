#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    while True:
        ports = range(1024)
        for port in ports:
            port = int(port)
            ports.append(port * 2)
        print(ports)
        time.sleep(1)