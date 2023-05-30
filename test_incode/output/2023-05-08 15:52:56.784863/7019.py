#!/usr/bin/python3
if __name__ == '__main__':
    #A program that opens user input.
    
    #Open the file that contains the user input.
    file = open('input.txt', 'r')
    
    #Read each line of the file into a list.
    lines = file.readlines()
    
    #Print each line of the file to the screen.
    for line in lines:
        print(line)
    
    #Close the file.
    file.close()
    
    #Close the terminal.
    terminal.close()

