#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads each line into a list
    for line in open("words.txt"):
        words.append(line.strip())
    #A while loop that prints each word in the list until it reaches the end of the list
    while len(words) > 0:
        print(words.pop(0))

