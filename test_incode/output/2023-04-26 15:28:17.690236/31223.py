#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and calculates user input. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the user input from the command line
    user = input("Enter your name: ")
    
    # Print the port number and the user input
    print("The port number is " + str(port) + " and your name is " + user)
    
