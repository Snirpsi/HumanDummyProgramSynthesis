#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    words = []
    
    for _ in range(port):
        words.append(input("Enter a word: "))
    
    print("\n".join(words))
    
