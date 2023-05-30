#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    numbers = []
    for word in words:
        numbers.append(int(word))
    
    numbers.sort()
    
    numbers = numbers * len(words)
    
    print('\n'.join(map(str, numbers)))
    
