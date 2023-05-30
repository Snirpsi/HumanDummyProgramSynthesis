#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
        
    print("\n".join(words))
    
