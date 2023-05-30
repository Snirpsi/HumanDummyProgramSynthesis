#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and prints words. """    
    
    words = input("Enter a word: ")
    
    for word in words.split():
        print(word)
        
