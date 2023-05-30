#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or converts a port. """    
    port = int(input("Enter a port: "))
    
    if port == -1:
        print("Invalid port")
        exit(1)
    
    ports = [port]
    
    while True:
        port = input("Enter a port: ")
        
        if port == -1:
            print("Invalid port")
            exit(1)
        
        if port in ports:
            print("Port already in use")
            exit(1)
        
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print(port)
    
