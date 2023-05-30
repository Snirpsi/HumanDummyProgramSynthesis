#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and iterates over user input. """    
    port = 0
    while True:
        port = input("Enter a port number: ")
        if port == 'exit':
            break
        else:
            print(port)
            
