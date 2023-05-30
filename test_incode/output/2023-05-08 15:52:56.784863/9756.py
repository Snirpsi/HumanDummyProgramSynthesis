#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    wordlist = input("Enter the words to remove: ")
    words = words.split()
    wordlist.sort()
    wordlist.reverse()
    wordlist.extend(words)
    print(" ".join(wordlist))

