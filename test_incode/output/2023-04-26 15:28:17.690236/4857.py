#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or prints all ports. """    
    port = 0
    while True:
        port = port + 1
        print("Port ", port, " is open.")
        time.sleep(1)
    
