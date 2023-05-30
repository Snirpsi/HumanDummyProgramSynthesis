#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or removes a list of words. """    
    while True:
        words = input("Enter a word: ")
        if words == "":
            break
        else:
            print(words * 