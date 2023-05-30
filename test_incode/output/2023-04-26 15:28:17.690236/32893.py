#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or enumerates a list of words. """    
    
    # Get the command line arguments
    commandLine = sys.argv[1:]
    
    # Parse the command line arguments
    commandLine = commandLine[1:]
    
    # Print the command line arguments
    print(commandLine)
    
    # Run the webserver
    webServer(commandLine)
    
