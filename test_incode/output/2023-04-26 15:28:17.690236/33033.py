#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or returns numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['a', 'b', 'c', 'd']
    
    numbers = []
    for word in words:
        try:
            number = int(word)
            numbers.append(number)
        except ValueError:
            pass
    
    print(numbers)
    
