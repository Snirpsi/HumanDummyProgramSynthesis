#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    wordlist = open("wordlist.txt","r")
    wordlist = wordlist.readlines()
    wordlist = wordlist[0].split()
    #A function that prints out the words in the list.
    print(" ".join(wordlist))
    #A function that prints out a random word from the list.
    print(random.choice(wordlist))

