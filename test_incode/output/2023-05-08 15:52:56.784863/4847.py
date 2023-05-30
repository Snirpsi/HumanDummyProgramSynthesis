#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes words.
    words_to_remove = ["hello","world","!"]
    for word in words:
        if word not in words_to_remove:
            print(word)
        else:
            print(word)

