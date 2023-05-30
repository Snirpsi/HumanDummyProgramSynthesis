#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or stores words. """    
    
    import sys
    
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for i in range(port):
        words.append(input("Enter a word: "))
    
    print(" ".join(words))
    
