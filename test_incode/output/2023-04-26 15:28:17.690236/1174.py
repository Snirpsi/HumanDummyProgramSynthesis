#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers and iterates over a port. """    
    port = sys.argv[1]
    while True:
        print(port)
        port = input("Enter a port number: ")
