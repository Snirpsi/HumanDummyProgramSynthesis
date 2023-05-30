#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or returns user input. """    
    
    words = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10"]
    
    while True:
        
        word = input("Enter a word: ")
        
        if word in words:
            words.remove(word)
            
        else:
            print("That word does not exist.")
            
