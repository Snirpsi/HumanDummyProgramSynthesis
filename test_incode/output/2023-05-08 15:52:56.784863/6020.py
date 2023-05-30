#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    wordlist = input("Enter the words to remove: ")
    words = words.split()
    wordlist = [word for word in wordlist if word not in words]
    print(" ".join(wordlist))

