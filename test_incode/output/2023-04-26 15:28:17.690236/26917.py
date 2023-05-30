#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or opens all ports. """    
    while True:
        time.sleep(1)
        print("\nFruits")
        fruits = open_fruits()
        print("\nOpen Ports")
        open_ports()
        print("\nClose Ports")
        close_ports()
        print("\nQuit")
        quit()
        
