#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        words = input("Enter a word: ")
        if words:
            words = words.split()
            for word in words:
                print(word, end=" ")
        else:
            break
