#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes words.
    while True:
        word = input("Enter a word: ")
        if word in words:
            words.remove(word)
        else:
            print("That word doesn't exist.")
            break

