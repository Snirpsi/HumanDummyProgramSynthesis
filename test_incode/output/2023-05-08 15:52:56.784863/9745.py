#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores a list of words.
    #It then prints them out in alphabetical order.
    words.sort()
    for word in words:
        print(word)

