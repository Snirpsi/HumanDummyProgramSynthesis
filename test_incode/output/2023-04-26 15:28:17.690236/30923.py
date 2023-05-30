#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or prints a list of numbers. """    
    
    words = input("Enter a list of words: ")
    
    words = words.split()
    
    words = [word for word in words if word not in 