#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        numbers = list(map(int, input().split()))
        numbers.sort()
        numbers.remove(numbers[0])
        print(numbers)
