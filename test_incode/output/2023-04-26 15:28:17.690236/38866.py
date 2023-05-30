#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or prints all ports. """    
    while True:
        ports = listen_ports()
        for port in ports:
            print(port)
        time.sleep(1)
        
