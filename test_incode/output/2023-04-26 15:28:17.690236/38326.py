#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print(number)
        else:
            break
