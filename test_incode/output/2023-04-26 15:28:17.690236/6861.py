#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or adds user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == 'quit':
            break
        else:
            print("The port number is:", port)
            
