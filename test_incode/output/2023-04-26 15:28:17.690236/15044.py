#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or multiplyes user input. """    
    port = int(input("Enter a port number: "))
    
    multiplier = 1
    
    for x in range(port):
        multiplier = multiplier * x
        
    print(multiplier)
    
