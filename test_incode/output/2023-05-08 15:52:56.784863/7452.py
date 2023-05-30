#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads words into it
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    print(words)

