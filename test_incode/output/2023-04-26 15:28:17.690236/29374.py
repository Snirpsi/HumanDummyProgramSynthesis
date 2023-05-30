#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and prints user input. """    
    words = input("Enter the words: ")
    words = words.split()
    for word in words:
        print(word)
        
