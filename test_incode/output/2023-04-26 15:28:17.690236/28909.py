#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or enumerates words. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            print(number * 2)
