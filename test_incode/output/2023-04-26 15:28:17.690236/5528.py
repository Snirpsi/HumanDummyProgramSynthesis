#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or enumerates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        if port % 2 == 0:
            print(port)
        else:
            print(port + 1)
            
