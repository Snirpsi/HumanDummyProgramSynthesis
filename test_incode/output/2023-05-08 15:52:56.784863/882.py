#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints the contents of the file.
    file = open('userinput.txt', 'r')
    print(file.read())
    file.close()

