#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers.sort()
    
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    
    for number in numbers:
        print(number)
    
    print('Done')

<|/ file filename=remove-numbers.py ext=.py |>