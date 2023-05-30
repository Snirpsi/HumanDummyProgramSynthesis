#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or converts user input. """    
    
    words = input("Enter the words to remove: ")
    
    words = words.split()
    
    words = [word for word in words if word not in words]
    
    print(" ".join(words))
    
