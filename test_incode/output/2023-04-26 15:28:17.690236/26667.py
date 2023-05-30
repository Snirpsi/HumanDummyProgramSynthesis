#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and calculates a list of numbers. """    
    while True:
        port = input("Enter a port number: ")
        numbers = range(port)
        print("The numbers are:")
        for number in numbers:
            print(number)
        print("