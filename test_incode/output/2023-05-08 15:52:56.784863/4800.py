#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    words_to_remove = ["hello","world","!"]
    words_to_remove.sort()
    words_to_remove.reverse()
    words_to_remove.extend(words)
    print(words_to_remove)

