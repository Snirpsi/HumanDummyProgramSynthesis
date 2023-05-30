#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and returns user input. """    
    
    words = input("Enter words to remove: ")
    
    words = words.split()
    
    words = [word for word in words if word not in 