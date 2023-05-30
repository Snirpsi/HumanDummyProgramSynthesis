#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and returns all ports. """    
    while True:
        words = input("Enter a word: ")
        ports = ""
        for word in words:
            ports += str(int(word) * 