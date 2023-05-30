#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints out the contents of that file.
    file = open('userinput.txt')
    for line in file:
        print(line)
    file.close()

