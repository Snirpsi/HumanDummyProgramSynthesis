#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and prints numbers. """    
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    i = 0
    
    while i < len(words):
        if words[i] in "0123456789":
            print(i)
            i = i + 1
        else:
            i = i + 1
            
