#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes words.
    words_to_remove = input("Enter the words to remove: ")
    words = words.split()
    words = filter(lambda x: x not in words_to_remove, words)
    print(" ".join(words))

