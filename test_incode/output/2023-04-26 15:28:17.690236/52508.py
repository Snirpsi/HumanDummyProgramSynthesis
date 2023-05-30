#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print("Your words are:")
    for word in words:
        print(word)
        
    print("\nThanks for playing!")
    
