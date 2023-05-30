#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    words = input("Enter the words: ")
    multiplied = []
    for word in words:
        multiplied.append(word*2)
    print(" ".join(multiplied))
<|/ file source=github ext=.py filename=