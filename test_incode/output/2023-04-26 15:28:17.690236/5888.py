#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == "exit":
            break
        else:
            print("Port number is", port)
            