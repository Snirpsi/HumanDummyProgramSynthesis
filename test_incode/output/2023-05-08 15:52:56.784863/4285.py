#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates words.
    #It will print out each word and how many times it appears.
    for word in words:
        print(word,words.count(word))

