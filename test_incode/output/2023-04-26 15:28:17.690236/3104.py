#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or removes fruits. """    
    
    words = input("Enter a word: ")
    
    if words in ["add", "addfruit"]:
        print("The word " + words + " has been added.")
    elif words in ["remove", "removefruit"]:
        print("The word " + words + " has been removed.")
    else:
        print("The word " + words + " is not recognized.")
        
