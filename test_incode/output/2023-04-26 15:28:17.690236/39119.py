#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and adds words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        words.append(word)
        
    print(" ".join(words))
    
