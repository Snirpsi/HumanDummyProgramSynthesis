#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that prints a list of words.
    for word in words:
        print(word)
    #A program that prints all the words in the list.
    for word in words:
        print(word)
    #A program that prints all the words in the list but in reverse order.
    for word in reversed(words):
        print(word)
    #A program that prints all the words in the list but in reverse order and in alphabetical order.
    for word in sorted(words):
        print(word)

