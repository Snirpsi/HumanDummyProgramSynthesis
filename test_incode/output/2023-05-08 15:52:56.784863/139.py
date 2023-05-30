#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.txt and prints out the contents of that file.
    file = open('user_input.txt', 'r')
    content = file.read()
    print(content)
    file.close()

