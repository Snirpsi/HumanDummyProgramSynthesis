#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads its content
    while True:
        line = input("Enter a word: ")
        if line == "":
            break
        print(line)
        #The word is appended to the list words and is printed out
        words.append(line)
    #The list is printed out
    print(words)

