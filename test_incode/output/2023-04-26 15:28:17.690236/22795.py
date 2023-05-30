#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or stores words. """    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        else:
            print(number)
