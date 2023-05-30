#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints every word in the file
    words = []
    for line in open("words.txt"):
        words.append(line.strip())
    for word in words:
        print(word)

