#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        numbers = input("Enter a number: ")
        numbers = list(map(int, numbers.split(',')))
        numbers.reverse()
        numbers = map(lambda x: x*x, numbers)
        print(*numbers, sep=',')
        
