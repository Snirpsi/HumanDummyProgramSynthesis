#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and returns all ports. """    
    ports = []
    while True:
        ports.append(random.randint(10000, 65535))
        print("Port 