#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports. """    
    while True:
        ports = listen_ports()
        for port in ports:
            convert(port)
        time.sleep(1)
