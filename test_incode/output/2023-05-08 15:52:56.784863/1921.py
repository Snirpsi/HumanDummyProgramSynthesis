#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates words.
    for index, word in enumerate(words):
        print(index, word)
    #A function that prints words in reverse order.
    for index, word in enumerate(reversed(words)):
        print(index, word)

