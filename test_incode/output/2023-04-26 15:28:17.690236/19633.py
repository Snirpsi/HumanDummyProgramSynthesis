#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and removes all ports. """    
    while True:
        port = input("Enter a port number: ")
        
        # Remove all ports
        remove_all_ports(port)

        # Multiply port
        multiply(port)

        # Print result
        print("The port multiplied is ", port)

        # Pause for user input
        pause()

# End of file

<|/ file ext=.py filename=