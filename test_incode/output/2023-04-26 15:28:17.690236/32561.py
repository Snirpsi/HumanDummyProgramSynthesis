#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or returns fruits. """    
    while True:
        port = input("Enter a port to remove or type 'exit' to exit: ")
        if port == 'exit':
            break
        else:
            remove_port(port)
            
    
<|/ file ext=.py filename=