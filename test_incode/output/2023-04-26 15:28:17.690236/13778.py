#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or iterates over words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
    else:
        
        words = input("Enter words to iterate: ")
        
    
    for word in words:
        
        print(word)
        
    
