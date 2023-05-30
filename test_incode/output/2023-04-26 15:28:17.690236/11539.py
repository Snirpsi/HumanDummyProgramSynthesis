#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and removes a port. """    
    
    # Read words from file
    words = open("words.txt", "r").read().split()
    
    # Remove port from words
    words = [word