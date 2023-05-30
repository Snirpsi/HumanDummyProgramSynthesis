#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and adds user input. """    
    port = int(input("Enter a port number: "))
    
    # Iterate over the port and add user input
    for port in range(port, 65535):
        print("Port number: ", port)
        print("Enter a number: ")
        number = int(input())
        print("The number is: ", number)
        
    # Close the port and quit the program
    