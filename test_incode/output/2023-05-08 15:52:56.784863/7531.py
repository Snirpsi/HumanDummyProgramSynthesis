#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and prints every word on a new line.
    while True:
        file = open("words.txt","r")
        for line in file:
            print(line)
        file.close()
        #A break that ends the while loop
        break

