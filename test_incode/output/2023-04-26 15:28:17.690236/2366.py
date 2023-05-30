#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and converts words. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        words = []
        for letter in port:
            if letter.isdigit():
                words.append(letter)
            else:
                words.append(letter + 