#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world', 'python', 'is', 'great']
    
    for word in words:
        print(word)
    
    if len(words) == 1:
        print('1')
    
    if len(words) == 2:
        print('