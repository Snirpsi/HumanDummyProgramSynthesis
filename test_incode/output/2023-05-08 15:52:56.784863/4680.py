#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    words = input("Enter a list of words: ")
    words = words.split()
    words = [word for word in words if word not in words]
    print(" ".join(words))

