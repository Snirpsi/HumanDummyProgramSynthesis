#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and iterates over a port. """    
    words = []
    port = 5000
    while True:
        words.append(input("Enter a word: "))
        port += 1
        if port > 65535:
            port = 5001
        print(port, "