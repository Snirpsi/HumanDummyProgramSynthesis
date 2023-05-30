#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or stores a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port: "))
        except ValueError:
            print("Invalid input. Try again.")
        else:
            ports.append(port)
            
