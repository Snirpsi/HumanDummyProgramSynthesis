#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes words.
    words_to_remove = input("Enter the words to remove: ")
    words_to_remove = words_to_remove.split()
    for word in words_to_remove:
        words = words.remove(word)
    print(words)

