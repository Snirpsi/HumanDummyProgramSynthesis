#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or enumerates user input. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        elif number < 10:
            print(number)
        else:
            print(number * 2)
            
