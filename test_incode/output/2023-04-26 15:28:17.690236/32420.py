#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    words_to_remove = []
    
    while True:
        
        word = input("Enter a word: ")
        
        if word == "":
            print("Goodbye!")
            break
        
        if word not in words:
            words_to_remove.append(word)
        
        else:
            print("You entered a word that isn't in the list. Try again.")
    
    for word in words_to_remove:
        words.remove(word)
    
    print(words)
    
