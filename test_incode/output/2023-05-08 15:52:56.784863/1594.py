#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    #The function then prints the words in reverse order.
    #The function then closes the list.
    wordlist = open("words.txt","r")
    wordlist = wordlist.readlines()
    wordlist = list(reversed(wordlist))
    print(wordlist)
    wordlist.close()
    #A function that opens a file, reads it, and prints it.
    wordlist = open("words.txt","r")
    print(wordlist.read())
    wordlist.close()

