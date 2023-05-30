#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or prints numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 999:
            break
        else:
            print(number)
    
