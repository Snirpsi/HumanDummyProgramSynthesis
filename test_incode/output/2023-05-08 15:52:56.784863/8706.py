#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints every word in the file
    words = [line.strip() for line in open('words.txt')]
    for word in words:
        print(word)

