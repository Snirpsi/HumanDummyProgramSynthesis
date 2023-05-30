#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and prints numbers. """    
    while True:
        print("Multiplication by ports:")
        ports = range(1,65535)
        for port in ports:
            print(port, "* ", ports[port])
        time.sleep(1)
        
