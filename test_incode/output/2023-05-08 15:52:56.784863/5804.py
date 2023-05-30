#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that adds a list of words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word not in words:
            print("Sorry, that word is not in the list")
        else:
            print(word)
            #print(words) #uncomment to print all words

