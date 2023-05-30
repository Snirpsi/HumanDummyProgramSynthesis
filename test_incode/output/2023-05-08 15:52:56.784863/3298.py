#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it.
    words = []
    with open("words.txt","r") as file:
        words = file.read().splitlines()
    print(words)

