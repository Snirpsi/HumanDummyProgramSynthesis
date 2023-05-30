#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    #The program will keep on printing until the user enters stop.
    while True:
        word = input("Enter a word: ")
        if word == "stop":
            break
        else:
            print(word)
            words.append(word)
    print(words)

