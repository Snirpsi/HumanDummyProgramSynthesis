#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that calculates a list of words.
    #It takes a list of words and returns them as a list.
    #The function takes the word list as a parameter.
    #The function then iterates through the words and checks
    #if the word is contained in the word list.
    #If the word is contained in the word list, then it adds
    #it to the word list.
    #If the word is not contained in the word list, then it adds
    #it to the word list.
    wordlist = ["hello","world","!"]
    wordlist = list(set(wordlist))
    wordlist = list(filter(lambda x: x in wordlist, wordlist))
    print(wordlist)

