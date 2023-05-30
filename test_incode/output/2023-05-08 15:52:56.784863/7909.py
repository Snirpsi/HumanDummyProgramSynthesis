#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes words.
    words = [x for x in words if x not in words]
    print(words)

