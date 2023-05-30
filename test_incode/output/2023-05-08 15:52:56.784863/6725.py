#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that adds a list of words.
    def add(words):
        return words[0] + words[1] + words[2]
    print(add(words))

