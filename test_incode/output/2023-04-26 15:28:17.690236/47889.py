#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        if word not in stopwords:
            print(word)
        else:
            print("That word is not in the stopwords list")
