#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that converts a list of words.
    def convert(words):
        return " ".join(words)
    print(convert(words))

