#!/usr/bin/python3
if __name__ == '__main__':
    #A function that converts user input.
    #It will take user input from the command line and print it out.
    #The function will take one parameter, the name of the file.
    #The function will then open the file and read it line by line.
    #The function will then print the line to the screen.
    #The function will then close the file.
    #The function will then exit the program.
    import sys
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            print(line)
            file.close()

