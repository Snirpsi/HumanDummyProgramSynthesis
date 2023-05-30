#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes words.
    for word in words:
        print(word)
        words.remove(word)
    #A endless loop that prints all the words.
    for word in words:
        print(word)

