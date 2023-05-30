#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that stores a list of words.
    #The program will exit when there are no more words to process.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in words:
            print(word)
        else:
            print("That word is not in the list")

