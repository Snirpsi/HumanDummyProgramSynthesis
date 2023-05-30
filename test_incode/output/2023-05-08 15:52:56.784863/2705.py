#!/usr/bin/python3
if __name__ == '__main__':
    #A function that opens user input.
    open_file = input("Enter the name of the file you want to open: ")
    
    #A function that opens the file specified and reads its contents.
    file = open(open_file, "r")
    
    #A function that prints the contents of the file.
    print(file.read())
    
    #A function that closes the file.
    file.close()

