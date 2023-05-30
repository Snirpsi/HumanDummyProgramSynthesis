#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    words = input("Enter the words: ")
    
    words = words.split()
    
    words.sort()
    
    for word in words:
        print(word)
    
