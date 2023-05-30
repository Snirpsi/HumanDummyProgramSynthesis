#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and converts user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
        
    print("\nThe words are:")
    
    for word in words:
        print(word)
        
    print("\nThe converted words are:")
    
    for word in words:
        print(word