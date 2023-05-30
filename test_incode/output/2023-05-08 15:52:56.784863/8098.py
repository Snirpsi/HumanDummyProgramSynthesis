#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that calculates words.
    #It takes a list of words and returns a list of words.
    #The function should also take in a word and return the word with that word replaced by "!".
    words = [word.replace("!","!") for word in words]
    print(words)

