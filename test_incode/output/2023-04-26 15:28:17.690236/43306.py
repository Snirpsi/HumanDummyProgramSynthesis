#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or opens a list of words. """    
    port = int(input("Enter a port number: "))
    words = input("Enter a list of words: ")
    
    if port > 0 and words != "":
        store