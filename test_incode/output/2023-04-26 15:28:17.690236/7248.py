#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and iterates over a list of words. """    
    
    words = input("Enter a word: ")
    
    words = [word for word in words.split() if word.isdigit()]
    
    for word in words:
        print(word)
    
    print("Done.")
    
