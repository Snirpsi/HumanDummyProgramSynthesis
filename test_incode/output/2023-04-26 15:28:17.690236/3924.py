#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and opens a list of numbers. """    
    port = 1
    numbers = []
    while True:
        numbers.append(port)
        port += 1
        print("Opening port " + str(port))
        open