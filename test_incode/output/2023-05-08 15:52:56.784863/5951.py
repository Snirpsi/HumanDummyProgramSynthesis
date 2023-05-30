#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    def enumerateWords(words):
        for index, word in enumerate(words):
            print(index, word)
    enumerateWords(words)

