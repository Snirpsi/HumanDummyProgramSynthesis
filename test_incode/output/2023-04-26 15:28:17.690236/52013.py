#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or returns numbers. """    
    while True:
        print("Enter a number: ")
        number = int(input())
        if number == -1:
            break
        else:
            print(number)
