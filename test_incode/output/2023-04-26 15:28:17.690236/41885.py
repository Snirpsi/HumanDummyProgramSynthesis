#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or removes numbers. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word.isdigit():
            
            print(word)
            
        else:
            
            print(word.replace(' ', '_'))
            
