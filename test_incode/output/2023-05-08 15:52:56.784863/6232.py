#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests a list of words.
    while True:
        wordlist = input("Enter a word: ")
        if wordlist == "":
            break
        else:
            wordlist.split()
            print(" ".join(wordlist))

