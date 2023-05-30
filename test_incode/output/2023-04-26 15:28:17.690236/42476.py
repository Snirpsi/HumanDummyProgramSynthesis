#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers and multiplyes user input. """    
    numbers = [int(i) for i in input().split()]
    numbers = [x*y for x,y in zip(numbers,numbers)]
    print(*numbers)
    
