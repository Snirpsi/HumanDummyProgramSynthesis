#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or prints all ports. """    
    
    ports = input("Enter the ports separated by spaces (ex: 123 456 789): ")
    
    for port in ports.split(" "):
        print(port)
    
