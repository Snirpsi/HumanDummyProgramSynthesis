#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    numbers = [int(i) for i in words]
    
    numbers_multiplied = [numbers[0]] * len(numbers)
    
    for number in numbers:
        numbers_multiplied.append(number * numbers[0])
    
    print(' '.join(map(str, numbers_multiplied)))
    
