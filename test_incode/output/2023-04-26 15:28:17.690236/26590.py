#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        words.append(word)
    print("\n".join(words))

<|/ file source=github filename=wordlist.py |>