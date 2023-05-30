#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or prints all ports. """    
    ports = openports()
    for port in ports:
        print(port)
        
