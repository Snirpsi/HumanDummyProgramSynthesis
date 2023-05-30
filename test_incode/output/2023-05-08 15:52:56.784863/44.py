#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores words.
    #The program will ask the user to input a word and store it in the
    #variable words. After the program has finished running, the program will
    #print the contents of words.
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            words.append(word)
    print(words)

