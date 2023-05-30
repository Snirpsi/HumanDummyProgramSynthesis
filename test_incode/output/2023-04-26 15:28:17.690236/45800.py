#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or returns a port. """    
    port = int(input("Enter a port number or press enter to quit: "))
    if port == -1:
        print("\nBye!")
        sys.exit()
    else:
        return port

<|/ file filename=port