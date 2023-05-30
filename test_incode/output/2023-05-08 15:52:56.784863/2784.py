#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes words.
    words = [w for w in words if w not in words]
    print(words)

