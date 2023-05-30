#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads lines from it
    words = []
    for line in open("words.txt"):
        words.append(line.strip())
    print(words)

