#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that iterates over a list of words.
    #It prints each word in the list one at a time.
    for word in words:
        print(word)
    #A function that prints a sentence with each word separated by a space.
    print(" ".join(words))

