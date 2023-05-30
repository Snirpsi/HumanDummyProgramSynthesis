#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes words.
    for word in words:
        words.remove(word)
    print(words)

