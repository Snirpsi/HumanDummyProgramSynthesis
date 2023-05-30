#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes words.
    while words:
        words.pop(0)
    print(words)

