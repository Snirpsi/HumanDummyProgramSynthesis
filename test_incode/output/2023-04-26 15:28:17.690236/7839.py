#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = input("Enter a word: ").split()
    total = 0
    for word in words:
        total += word
    print(total)
