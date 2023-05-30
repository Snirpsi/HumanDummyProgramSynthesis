#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    for word in words:
        word = word.strip()
        
        if word:
            print(word)
            
