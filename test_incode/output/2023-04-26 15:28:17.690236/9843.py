#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or stores a port. """    
    
    port = None
    
    try: 
        port = int(input("Enter a port number: "))
    except ValueError: 
        print("Please enter a number!")
        
    if port is not None:
        print("Opening port", port)
        
        try: 
            