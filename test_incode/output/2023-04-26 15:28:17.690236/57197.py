#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port and stores a list of words. """    
    port = int(input("Enter a port number: "))
    words = []
    for _ in range(port):
        words.append(input("Enter a word: "))
    print(words)
    
