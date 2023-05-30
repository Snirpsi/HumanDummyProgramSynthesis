#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and stores fruits. """    
    
    import sys
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word.lower())
        
    fruits = []
    
    for word in words:
        if word not in fruits:
            fruits.append(word)
            
    print("\n".join(