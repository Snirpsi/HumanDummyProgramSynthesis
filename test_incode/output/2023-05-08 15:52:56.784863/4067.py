#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that converts words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            print("Goodbye!")
            break
        else:
            print(word, "is a word!")

