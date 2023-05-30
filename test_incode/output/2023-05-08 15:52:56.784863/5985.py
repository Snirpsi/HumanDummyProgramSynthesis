#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.
    
    #Open the file.
    file = open("input.txt", "r")
    
    #Read in the file.
    lines = file.readlines()
    
    #Print the lines.
    for line in lines:
        print(line)
    
    #Close the file.
    file.close()

