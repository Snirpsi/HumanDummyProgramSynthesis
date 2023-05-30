#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    
    words = input("Enter a word: ")
    words = words.split()
    
    for word in words:
        print(word)
        
    print("Done.")
    
