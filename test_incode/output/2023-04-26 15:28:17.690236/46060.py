#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or removes a port. """    
    while True:
        port = int(input("Enter a port: "))
        if port == -1:
            break
        
        ports.append(port)
        
        if port == len(ports):
            break
        
        ports.pop(port)
        
        print("Port ", port, " has been added.")
        
    print("\nThe ports 