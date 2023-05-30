#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and removes user input. """    
    
    # Read user input from stdin
    line = sys.stdin.readline()
    
    # Remove user input
    line = line.strip()
    
    # Print user input
    print(line)
    
    # Print result
    print(line)
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Close all files
    for file in [sys.stdin, sys.stdout, sys.stderr]:
        file.close()
    
    # Exit program
    sys.exit(0)

<|/ file filename=remove-user-input.py ext=.py |>