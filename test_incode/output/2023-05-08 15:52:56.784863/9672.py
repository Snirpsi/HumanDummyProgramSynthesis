#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that stores a list of words.
    #The loop will run until the user enters EOF.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            words.append(word)
    print(words)

