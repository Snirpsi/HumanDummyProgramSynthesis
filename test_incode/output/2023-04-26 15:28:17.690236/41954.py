#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers and stores a list of words. """    
    import sys
    
    numbers = sys.argv[1:]
    
    words = []
    
    for number in numbers:
        words.append(str(number))
    
    print("\n".join(words))
    
