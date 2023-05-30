#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
