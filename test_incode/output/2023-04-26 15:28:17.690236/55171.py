#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and multiplyes a list of words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    multiplier = []
    
    for word in words:
        multiplier.append(word*2)
        
    print(multiplier)
    
