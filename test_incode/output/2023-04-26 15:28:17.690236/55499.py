#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or converts a port. """    
    
    # Get the port number
    port = int(input("Enter the port number: "))
    
    # Get the number or port
    number = int(input("Enter the number or port: "))
    
    # Multiply or convert the number
    if number % 2 == 0:
        number = number * 2
    else:
        number = number * 