#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        print("Open fruits:")
        fruits = input("\n").split()
        for fruit in fruits:
            print("\t" + fruit)
