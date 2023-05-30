#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or returns a list of numbers. """    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print('Usage: python enumerate_numbers.py <number>')
            sys.exit()
    
    print('Numbers:')
    for number in numbers:
        print(number)
    
    print('Done.')
    
