#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        word = word.strip()
        
        if word != '':
            
            print(word)
            
        else:
            
            print('')
            
