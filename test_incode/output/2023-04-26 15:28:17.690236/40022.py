#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or adds user input. """    
    while True:
        word1 = input("Enter a word: ")
        word2 = input("Enter another word: ")
        
        if word1 == word2:
            print("They are equal")
        else:
            print("They are not equal")
        
