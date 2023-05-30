#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or opens fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['apple', 'banana', 'orange', 'kiwi']
    
    for word in words:
        print(word)
        
