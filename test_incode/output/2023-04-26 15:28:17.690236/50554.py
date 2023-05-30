#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports and adds a list of words. """    
    ports = Ports()
    ports.start()
    words = []
    while True:
        words.append(input("Enter a word: "))
        ports.