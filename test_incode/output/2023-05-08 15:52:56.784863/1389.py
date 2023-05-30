#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that removes words.
    words = [word for word in words if word not in words]
    print(words)

