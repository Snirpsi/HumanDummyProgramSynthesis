#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        word = word.lower()
        if word not in stopwords:
            print(word)
            