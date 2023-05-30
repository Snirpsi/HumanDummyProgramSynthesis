#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    for index, word in enumerate(words):
        print(index, word)
    #A function that prints the indexes and the words in the list.
    print(enumerate(words))

