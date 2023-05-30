#!/usr/bin/python3
if __name__ == '__main__':
    #A function that returns user input.
    #The user input will be the name of the file to be read.
    #The function will then return the name of the file read by the user.
    filename = input("Enter the name of the file to be read: ")
    
    #The function will then return the contents of the file read by the user.
    file = open(filename, "r")
    
    #The function will then print the contents of the file read by the user.
    print(file.read())
    file.close()
    

