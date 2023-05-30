#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and prints a port. """    
    
    port = 1
    
    while True:
        port = input("Enter a port number: ")
        
        if port == '':
            break
        
        print(port)
        
    print("Done")
    
