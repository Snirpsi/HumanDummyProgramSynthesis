#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and prints every word on a new line.
    for line in open("words.txt"):
        print(line)
        #A for loop that prints every word on a new line.
        for word in line.split():
            print(word)
            #A while loop that prints every word on a new line.
            while word != "":
                print(word)
                word = input("Enter a word: ")
            #A break statement that breaks out of the while loop.

