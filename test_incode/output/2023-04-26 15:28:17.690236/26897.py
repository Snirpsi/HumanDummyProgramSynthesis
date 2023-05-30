#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and removes user input. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'q':
            break
        
        if word not in words:
            words.append(word)
            
    print("\n".join(words))
    
    
