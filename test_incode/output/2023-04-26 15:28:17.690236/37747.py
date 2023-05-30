#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number > 0 and number <= 10:
            print(number)
        else:
            print("Invalid number")
