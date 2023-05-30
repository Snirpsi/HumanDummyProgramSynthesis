#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and iterates over user input. """    
    
    words = []
    
    while True:
        
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print("You entered", len(words), "words")
    
    for word in words:
        print(word)
        
