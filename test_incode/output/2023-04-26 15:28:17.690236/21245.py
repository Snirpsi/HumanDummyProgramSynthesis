#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        print("Opening fruits...")
        fruits = open_fruits()
        print("Closing fruits...")
        fruits.close()
        print("Closing 