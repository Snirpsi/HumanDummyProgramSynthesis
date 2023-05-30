#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        words = input().split()
        for word in words:
            print(word)
