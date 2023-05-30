#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that adds a list of words.
    def add(words):
        words.extend(["!"])
        return words
    print(add(words))

