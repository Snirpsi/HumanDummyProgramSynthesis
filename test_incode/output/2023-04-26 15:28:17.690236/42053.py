#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input. """    
    
    # Create a program object
    program = Program()
    
    # Parse the command line arguments
    program.parse()
    
    # Run the program
    program.run()
    
    # Print the result
    program.print_result()
    
    # 