#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or prints fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    fruits = ['apple', 'banana', 'cherry']
    
    for word in words:
        if word in fruits:
            print('{} is a fruit'.format(word))
        else:
            print('{} is not a fruit'.format(word))
    
