#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
    else:
        
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
    for word in words:
        
        print(word*10)
        
