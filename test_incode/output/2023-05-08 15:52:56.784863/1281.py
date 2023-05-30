#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens a list of words.
    for word in words:
        print(word)
        #A loop that prints one word at a time.
        for letter in word:
            print(letter)
        #A loop that prints a newline after each word.
        print()

