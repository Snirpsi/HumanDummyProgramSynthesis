#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or multiplyes a list of words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word == '':
            continue
        
        number = int(word)
        
        if number == 1:
            print(1)
            continue
        
        number *= 