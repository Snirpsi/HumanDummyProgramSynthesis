#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or iterates over user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'q':
            break
        
        words.append(word)
    
    print("\n".join(words))
    
