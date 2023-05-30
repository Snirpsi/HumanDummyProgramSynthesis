#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and removes a list of numbers. """    
    while True:
        words = open('words.txt').read().splitlines()
        words = [word for word in words if word not in 