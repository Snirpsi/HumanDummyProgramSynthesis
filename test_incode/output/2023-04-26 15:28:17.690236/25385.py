#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers. """    
    numbers = sys.argv[1:]
    numbers = list(map(int, numbers))
    numbers = list(filter(lambda x: x not in numbers, numbers))
    print(numbers)
    
