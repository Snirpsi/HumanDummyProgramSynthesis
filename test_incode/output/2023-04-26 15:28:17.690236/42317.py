#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and multiplyes a port. """    
    while True:
        print("List of numbers:")
        for num in range(1,11):
            print("  ", num)
        print("Multiplying port:")
        port = int(input("Port: "))
        port *= 2
        print("  ", port)
        print("