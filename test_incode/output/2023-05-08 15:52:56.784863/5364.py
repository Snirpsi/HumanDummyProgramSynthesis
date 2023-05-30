#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints out the contents of that file
    file = open('userinput.txt', 'r')
    content = file.read()
    print(content)
    file.close()

