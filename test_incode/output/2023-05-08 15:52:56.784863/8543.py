#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes a list of words.
    while True:
        word = input("Enter a word: ")
        if word in words:
            words.remove(word)
        else:
            print("That word is not in the list")
            break

