#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or returns words. """    
    
    ports = input("Enter the ports: ")
    words = ""
    
    for port in ports.split(","):
        words = words + port
    
    print(words)
    
