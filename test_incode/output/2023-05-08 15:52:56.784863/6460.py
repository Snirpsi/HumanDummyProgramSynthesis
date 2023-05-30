#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that adds words.
    def add(words):
        return words + ["!"]
    print(add(words))

