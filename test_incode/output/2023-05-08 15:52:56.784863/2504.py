#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that converts words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        print(word, "is", end="")
        words = words + [word]
    print(words)

