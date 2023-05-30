#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or opens fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 fruits.py [words]")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        fruit = Fruit(word)
        
        if fruit.is_