#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes words.
    while True:
        word = input("Enter a word: ")
        if word in words:
            words.remove(word)
        else:
            break
    print(words)

