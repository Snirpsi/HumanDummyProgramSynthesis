#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or stores numbers. """    
    
    ports = []
    
    while True:
        try:
            port = int(input("Enter a port: "))
            ports.append(port)
        except ValueError:
            print("Invalid input. Try again.")
    
    for port in ports:
        print(port)
    
