#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    
    words = input("Enter words: ")
    
    words = words.split()
    
    words.extend(["a", "b", "c", "d", "e"])
    
    print(" ".join(words))
    
