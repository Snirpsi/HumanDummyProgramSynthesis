#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or returns fruits. """    
    
    words = []
    fruits = []
    
    while True:
        
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        fruits.append(word)
        
        words.append(word)
        
        print("The word {} is {}".format(word, fruit