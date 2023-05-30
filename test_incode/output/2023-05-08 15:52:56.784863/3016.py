#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that adds words.
    for word in words:
        print(word,end="")
    #The program will ask for an input.
    word = input("Enter a word: ")
    #The program will print out the word and the input word.
    print(word,word)

