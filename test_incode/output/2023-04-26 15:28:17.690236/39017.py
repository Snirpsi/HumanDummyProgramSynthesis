#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        word = input("Enter a word: ")
        word = word.lower()
        if word not in stopwords:
            print(word)
        else:
            print("That word is not in the stopwords list")
