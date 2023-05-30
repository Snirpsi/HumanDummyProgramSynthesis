#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        port = random.randint(10000, 65535)
        print("Port 