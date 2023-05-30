#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates words.
    while True:
        words.append(input("Enter a word: "))
        print(words)
        print("-"*50)

