#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    words_to_remove = input("Enter the words to remove: ")
    words_to_remove = words_to_remove.split()
    words_to_remove.sort()
    words_to_remove = " ".join(words_to_remove)
    print(words_to_remove)

