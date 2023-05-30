#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports and opens fruits. """    
    while True:
        ports = open_fruits()
        for port in ports:
            print(port)
        time.sleep(1)
