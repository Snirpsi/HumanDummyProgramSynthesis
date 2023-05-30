#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        elif number.isdigit():
            print(int(number) * 2)
        else:
            print(int(number))
