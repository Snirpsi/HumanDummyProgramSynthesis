#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    with open('words.txt', 'r') as file:
        words = file.read().split()
    print(words)

