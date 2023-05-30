#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and opens user input. """    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            words.append(word)
    print(" ".join(words))

<|/ file filename=wordlist.py ext=.py |>