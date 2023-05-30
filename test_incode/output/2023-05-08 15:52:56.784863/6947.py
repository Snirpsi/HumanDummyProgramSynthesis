#!/usr/bin/python3
if __name__ == '__main__':
    #A function that opens user input.
    #The user input will be the name of the file.
    filename = input("Enter the name of the file: ")
    
    #A function that opens the file.
    file = open(filename, "r")
    
    #A function that reads the file.
    lines = file.readlines()
    
    #A function that prints the lines.
    for line in lines:
        print(line)
    
    #A function that closes the file.
    file.close()

