#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        words = word.split()
        for word in words:
            if word not in stopwords:
                