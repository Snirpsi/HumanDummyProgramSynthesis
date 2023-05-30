#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or removes a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            print("Port number 