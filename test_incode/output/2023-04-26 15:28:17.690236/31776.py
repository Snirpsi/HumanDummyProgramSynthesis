#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers or opens words. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = map(int, numbers)
    
    words = []
    
    for number in numbers:
        words.append(str(number))
    
    sys.stdout.write('\n'.join(words))
    
