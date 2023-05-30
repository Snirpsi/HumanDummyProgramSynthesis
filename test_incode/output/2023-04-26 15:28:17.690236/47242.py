#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        
        # Read user input from stdin
        line = sys.stdin.readline()
        
        # Print the line to stdout
        print(line)
        
        # Break the loop if the user enters ctrl-c
        if line == '':
            break
        
        # 