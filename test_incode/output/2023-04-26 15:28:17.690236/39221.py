#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = sys.argv[1:]
    
    multiplier = 1
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
