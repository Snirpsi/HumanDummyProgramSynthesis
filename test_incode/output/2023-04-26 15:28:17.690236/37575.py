#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports and converts a list of words. """    
    ports = []
    words = input("Enter a list of words: ")
    for word in words.split():
        ports.append(int(word))
    ports.sort()
    print(ports)

<|/ file source=github ext=.py |>