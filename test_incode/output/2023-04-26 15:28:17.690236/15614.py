#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or prints a list of words. """    
    port = int(input("Enter a port number: "))
    words = []
    
    while port > 0:
        words.append(input("Enter a word: "))
        port -= 1
    
    print(" ".join(words))
    
