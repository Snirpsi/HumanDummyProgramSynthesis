#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that adds a list of words.
    while True:
        words.append(input("Enter a word: "))
        #A while loop that prints the words to the screen.
        while words:
            print(" ".join(words))
            words.pop(0)

