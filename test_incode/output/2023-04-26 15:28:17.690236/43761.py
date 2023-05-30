#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or prints a list of numbers. """    
    
    ports = []
    
    while True:
        ports.append(input("Enter a port number: "))
        
        if ports[-1] == "q":
            break
        
    print("\n".join(map(str, ports)))
    
