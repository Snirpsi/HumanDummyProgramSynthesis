#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port and enumerates user input. """    
    port = int(input("Enter a port number: "))
    
    # Enumerate user input
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter == input("Enter a letter: "):
            print(letter)
            
    # Print the port number
    print("The port number is:", port)
    
    # Close the program
    exit()
    
# End of program
