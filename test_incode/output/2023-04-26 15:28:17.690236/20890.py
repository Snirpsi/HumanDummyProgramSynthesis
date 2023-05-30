#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates fruits or opens a port. """    
    
    fruit = input("Enter fruit or open a port: ")
    
    if fruit == "fruit":
        fruit()
    elif fruit == "open":
        openPort()
    else:
        print("Invalid input")
        
