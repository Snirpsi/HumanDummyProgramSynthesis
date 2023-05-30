#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and iterates over a list of numbers. """    
    
    port = 1
    
    while(True):
        
        number = input("Enter a number: ")
        
        port.write(str(number))
        
        port.flush()
        
        number = port.read()
        
        print(number)
        
        port.close()
        
        port.