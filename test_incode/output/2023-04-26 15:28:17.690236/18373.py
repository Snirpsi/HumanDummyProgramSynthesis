#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0: break
        if number % 2 == 0:
            print(number)
        else:
            print(number - 1)
