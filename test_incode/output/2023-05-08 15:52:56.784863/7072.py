#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that returns words.
    while True:
        print(words)
        words = input("Enter a word: ")
        if words:
            break

