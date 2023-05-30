#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and stores a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python multiply_words.py words.txt")
        exit(1)
    
    with open(sys.argv[1]) as words:
        words = [word.strip() for word in words]
    
    port = 0
    
    for word in words:
        port *= int(word)
    
    print(port)
    
