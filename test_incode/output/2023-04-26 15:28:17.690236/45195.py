#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or enumerates user input. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number. Try again.")
        else:
            break
    
    print("The port number you entered is", port)

<|/ file ext=.py filename=port