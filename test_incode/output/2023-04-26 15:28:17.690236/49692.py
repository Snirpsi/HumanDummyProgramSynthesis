#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or converts a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            print("Ending program.")
            break
        else:
            print("Converting number to 