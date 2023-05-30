#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 words.py")
        exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.lower()
        word = word.strip()
        word = word.split()
        
        word = ""
        for word in word:
            word = word + " "
        
        print(word)
        
