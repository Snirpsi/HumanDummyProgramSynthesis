#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers and removes all ports. """    
    ports = input("Enter the ports you want to remove: ").split()
    ports_number = int(input("Enter the number you want to multiply by: "))
    
    ports_number *= int(input("Enter the number you want to multiply by: "))
    
    for port in ports:
        if port in ports_number:
            ports_number = ports_number - int(port)
    
    print("The ports number is: " + str(ports_number))
    
