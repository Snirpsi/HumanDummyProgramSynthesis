#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and opens user input. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if word == "quit":
            break
        
    print("\n".join(words))
    
    
