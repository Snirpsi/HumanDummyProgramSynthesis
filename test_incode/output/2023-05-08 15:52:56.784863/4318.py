#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads lines from it
    for line in open("words.txt"):
        #For each line in the file, check if it contains the word "hello"
        if line.find("hello") != -1:
            print(line)
            #If it does, print it
        else:
            #If it doesn't, print a space
            print(" ")

