#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and iterates over numbers. """    
    port = int(input("Enter a port number: "))
    
    # Iterate over numbers and multiply them
    for num in range(1, port+1):
        print(num*num)
        
    # Close the program 