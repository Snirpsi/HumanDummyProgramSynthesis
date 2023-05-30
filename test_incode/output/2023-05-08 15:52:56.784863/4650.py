#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that enumerates a list of words.
    for index, word in enumerate(words):
        print(word, end=' ')
        if index == len(words)-1:
            print("\n")

