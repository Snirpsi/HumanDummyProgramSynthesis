#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        words = word.split(' ')
        
        for word in words:
            word = word.strip()
            
            if word != '':
                