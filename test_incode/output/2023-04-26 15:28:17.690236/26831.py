#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or converts a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        if arg == '--help':
            print(__doc__)
            sys.exit(0)
        else:
            words.append(arg)
    
    numbers = []
    for word in words:
        try:
            number = int(word)
            numbers.append(number)
        except ValueError:
            pass
    
    numbers = list(set(numbers))
    numbers.sort()
    
    for number in numbers:
        print(number)
    
