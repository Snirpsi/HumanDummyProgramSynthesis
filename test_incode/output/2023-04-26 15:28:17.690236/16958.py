#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and removes numbers. """    
    while True:
        port = int(input("Enter a port to multiply and remove numbers: "))
        number = int(input("Enter a number to multiply: "))
        
        if port == 0 or number == 0:
            print("No numbers entered")
        elif port == number:
            print("The number you entered is already in the port")
        else:
            number *= port
            
            print("The port multiplied by {} is {}".format(port, number))
            
