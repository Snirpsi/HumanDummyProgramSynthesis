#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and prints user input. """    
    ports = range(1,65535)
    for port in ports:
        print("Enter port " + str(port) + " 