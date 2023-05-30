#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input or enumerates all ports. """    
    
    # Read input from stdin and parse it as JSON
    ports = json.loads(sys.stdin.read())
    
    # Print all ports
    for port in ports:
        print(port)
        
    # Print all ports 