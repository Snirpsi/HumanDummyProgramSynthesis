#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and converts user input. """    
    
    # Remove user input from command line
    sys.argv = sys.argv[1:]
    
    # Convert user input to a float
    number = float(sys.argv[1])
    
    # Print the result
    print("The number is", number)
    
    # Exit the program
    sys.exit()
    
