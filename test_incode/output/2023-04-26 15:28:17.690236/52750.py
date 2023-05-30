#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or returns all ports. """    
    while True:
        ports = listen_ports()
        for port in ports:
            print(port)
        time.sleep(1)
    
