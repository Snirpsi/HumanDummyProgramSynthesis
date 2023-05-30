#!/usr/bin/python3
if __name__ == '__main__':
    #A function that returns user input.
    #It will ask the user for input until the user enters q to quit.
    import sys
    
    while(True):
        command = input("Enter command: ")
        
        if command == "q":
            sys.exit()
        
        else:
            print(command)

