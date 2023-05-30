#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in words:
            print(word + " already exists")
        else:
            words.add(word)
            print(word + " added")
    else:
        print("Usage: python word