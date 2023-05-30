#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    #The program will keep asking the user for input until the user enters 
    #the word "quit".
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            words.append(word)
    print(words)

