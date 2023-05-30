#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests a list of words.
    while True:
        wordlist = input("Enter a word: ")
        if wordlist == "":
            break
        wordlist = wordlist.split()
        for word in wordlist:
            if word in words:
                print(word)
            else:
                print("That word is not in the list")

