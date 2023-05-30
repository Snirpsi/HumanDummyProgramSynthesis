#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes a list of words.
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            words.append(word)
    print(" ".join(words))

