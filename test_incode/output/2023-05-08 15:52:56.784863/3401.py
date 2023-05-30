#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    wordlist = open("wordlist.txt","r")
    #A function that reads a word from the list.
    word = wordlist.read()
    #A function that prints the word in the list.
    print(word)
    #A function that prints the word in the list with a space between each word.
    print(" ".join(word))

