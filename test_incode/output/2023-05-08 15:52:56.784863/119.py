#!/usr/bin/python3
if __name__ == '__main__':
    #A function that requests user input.
    #The user input will be the name of the file.
    file = input("Enter the name of the file you want to open: ")
    file = open(file, "r")
    
    #A function that prints the contents of the file.
    #The file will be opened and read in as a string.
    content = file.read()
    print(content)
    file.close()

