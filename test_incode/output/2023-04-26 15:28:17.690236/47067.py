#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and opens fruits. """    
    words = open("fruits.txt").read().split()
    for word in words:
        print(word)
