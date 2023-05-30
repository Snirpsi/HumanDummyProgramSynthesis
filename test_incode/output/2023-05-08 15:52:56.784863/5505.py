#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads words from it
    words = []
    with open('words.txt', 'r') as f:
        words = f.read().split()
    print(words)

