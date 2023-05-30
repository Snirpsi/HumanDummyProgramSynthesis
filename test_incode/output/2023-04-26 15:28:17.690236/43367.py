#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 10:
            print(number)
        elif number < 100:
            print(number * 2)
        elif number < 1000:
            print(number * 3)
        elif number < 10000:
            print(number * 4)
        elif number < 100000:
            print(number * 5)
        elif number < 1000000:
            print(number * 6)
        elif number < 10000000:
            print(number * 7)
        elif number < 100000000:
            print(number * 8)
        elif number < 1000000000:
            print(number * 9)
        else:
            break
