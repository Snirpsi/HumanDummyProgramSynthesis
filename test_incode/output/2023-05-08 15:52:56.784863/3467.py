#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints all the words in it
    words = [line.strip() for line in open("words.txt")]
    for word in words:
        print(word)

