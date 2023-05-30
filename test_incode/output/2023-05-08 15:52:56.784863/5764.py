#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests words.
    while True:
        print(" ".join(words))
        words = input("Enter a word: ")
        #A break if the user enters EOF.
        if words == "":
            break
        #A break if the user enters EOF.
        if words == "":
            break

