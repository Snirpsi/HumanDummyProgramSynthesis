#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads its content
    wordlist = open(words.txt,'r')
    words = wordlist.readlines()
    wordlist = wordlist.close()
    #A function that prints all the words in the file
    for word in words:
        print(word)

