#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads its content
    while True:
        line = input("Enter a word: ")
        if line == "":
            break
        if line not in words:
            print("That word is not in the list")
        else:
            print(line)

