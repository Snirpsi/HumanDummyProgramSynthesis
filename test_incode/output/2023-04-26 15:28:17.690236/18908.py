#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and removes fruits. """    
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    words = filter(lambda x: x not in ["apple", "banana", "cherry"], words)
    
    print("The words ", words, " are 