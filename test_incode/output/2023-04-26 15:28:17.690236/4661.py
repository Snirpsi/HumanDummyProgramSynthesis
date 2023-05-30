#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or returns fruits. """    
    while True:
        fruits = convert_port()
        if fruits == 'exit':
            break
        else:
            print(