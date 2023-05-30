#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and calculates a list of words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
    
    print("\nThe words are:")
    
    for word in words:
        print(word)
    
    print("\nThe average word length is " + str(len(word