#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that converts a list of words.
    #The program will keep looping until the user enters stop.
    while True:
        word = input("Enter a word: ")
        if word == "stop":
            break
        else:
            print(words[words.index(word)])

