#!/usr/bin/python3
if __name__ == '__main__':
    #A function that opens user input.
    open_file = input("Enter the file name: ")
    
    #A function that reads the file line by line.
    lines = open(open_file).readlines()
    
    #A function that prints the lines.
    for line in lines:
        print(line)
    
    #A function that closes the file.
    lines.close()

