#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or removes a list of numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        if port in ports:
            print(port)
        else:
            ports.remove(port)
            print("Port removed")
