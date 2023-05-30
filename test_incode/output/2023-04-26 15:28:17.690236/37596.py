#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or adds a port. """    
    
    port = int(input("Enter a port: "))
    
    if port > 0:
        print("The port is greater than zero!")
    else:
        print("The port is less than zero!")
    
