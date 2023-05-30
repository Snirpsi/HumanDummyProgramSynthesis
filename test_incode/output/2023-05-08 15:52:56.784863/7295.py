#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints out the contents of that file.
    file = open('input.txt', 'r')
    for line in file:
        print(line)
    file.close()

