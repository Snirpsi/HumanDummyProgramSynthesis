#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    with open(words.txt) as file:
        words = file.read().splitlines()
    #A function that prints all the words in words
    for word in words:
        print(word)

