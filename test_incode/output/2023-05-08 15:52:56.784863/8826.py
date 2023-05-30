#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints the contents of that file.
    file = open('userinput.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()

