#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    #It then prints the words in reverse order.
    #It then closes the file.
    wordlist = open("wordlist.txt","r")
    wordlist = wordlist.readlines()
    wordlist.close()
    wordlist = wordlist[::-1]
    for word in words:
        print(word,end="")
    print("")
    wordlist.close()

