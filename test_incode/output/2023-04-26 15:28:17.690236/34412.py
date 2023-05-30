#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    
    words = sys.argv[1:]
    
    for word in words:
        
        word = word.strip()
        
        if word == '':
            continue
        
        if word in 