#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words and prints a list of words. """    
    
    words = input("Enter the words to be removed: ")
    
    words = words.split()
    
    words = [word for word in words if word not in words]
    
    print(words)
    
