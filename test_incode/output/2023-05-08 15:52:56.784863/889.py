#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests words.
    while True:
        word = input("Enter a word: ")
        if word in words:
            print(word)
        else:
            print("Sorry, I didn't find that word.")

