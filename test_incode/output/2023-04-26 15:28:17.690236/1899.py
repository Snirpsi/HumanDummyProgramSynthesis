#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world', 'python', 'is', 'fun']
    
    print('\n'.join(words))
    
    print('\n'.join([' '.join(word) for word in words]))
    
    print('\n'.join([' '.join(word) for word in words if len(word) > 2]))
    
    print('\n'.join([' '.join(word) for word in words if len(word) > 3 and word[-1] == '