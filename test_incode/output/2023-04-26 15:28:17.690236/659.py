#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    while True:
        numbers = []
        for i in range(1, 10):
            numbers.append(i)
        print('\n'.join(map(str, numbers)))
