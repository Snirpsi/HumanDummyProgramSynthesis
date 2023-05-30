#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that removes words.
    def remove(words):
        for word in words:
            words.remove(word)
    return remove

