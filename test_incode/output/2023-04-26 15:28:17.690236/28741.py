#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers. """    
    while True:
        print('The numbers are:')
        numbers = [int(x) for x in input().split()]
        for number in numbers:
            print(number)
