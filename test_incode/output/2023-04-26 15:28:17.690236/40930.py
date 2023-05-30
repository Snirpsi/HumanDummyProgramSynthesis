#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or prints words. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0: break
        if number % 2 == 0:
            print(number * 2)
        else:
            print(number * 