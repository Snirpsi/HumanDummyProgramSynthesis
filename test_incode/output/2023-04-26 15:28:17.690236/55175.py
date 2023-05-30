#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or iterates over words. """    
    while True:
        port = input("Enter a port number: ")
        if port == "exit":
            break
        else:
            print(port)
    
<|/ file filename=