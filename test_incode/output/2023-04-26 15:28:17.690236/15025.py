#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or stores words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if len(word) == 0 or word[-1] == '\n':
            break
        
    words.sort()
    
    print("\n".join(words))
    
