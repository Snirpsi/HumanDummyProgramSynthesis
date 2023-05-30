#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    #The loop will run until the user enters CTRL-C.
    while True:
        words.append(input("Enter a word: "))
        if input("Enter a word: ") == "exit":
            break
    print(words)

