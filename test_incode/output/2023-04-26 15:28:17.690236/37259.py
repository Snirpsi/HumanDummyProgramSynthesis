#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and multiplyes user input. """    
    
    words = input("Enter the words to remove: ")
    
    words = words.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word not in 