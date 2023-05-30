#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads one line at a time
    for line in open("words.txt"):
        #A for loop that prints each word on a new line
        for word in line.split():
            print(word)
        #A while loop that prints the next word in the file
        while 1:
            word = input("Enter a word: ")
            if word == "":
                break
            print(word)
        #A break that ends the program
        break

