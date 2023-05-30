#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and prints numbers. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        print(port)
        
