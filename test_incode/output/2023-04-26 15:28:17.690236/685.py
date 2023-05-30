#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words or prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'hello'
        
    print(word)
    
