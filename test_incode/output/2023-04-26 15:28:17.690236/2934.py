#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and returns a list of numbers. """    
    port = []
    while True:
        port.append(int(input("Enter a port number: ")))
        if port == []:
            break
    print(port)
