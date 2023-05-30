#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and stores words. """    
    
    port = 0
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    words.sort()
    
    for word in words:
        
        port += 1
        
        