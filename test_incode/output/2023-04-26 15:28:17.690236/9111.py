#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and converts words. """    
    while True:
        port = int(input("Enter a port number: "))
        words = input("Enter a word: ").split()
        for word in words:
            print(word, 