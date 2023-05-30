#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or converts a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number")
            continue
        else:
            break
    
    ports = [port]
    
    while True:
        try:
            ports.append(int(input("Enter a port number: ")))
        except ValueError:
            print("Invalid port number")
            continue
        else:
            break
    
    ports.sort()
    
    for port in ports:
        print("Port number {} is {}".format(port, port+1))
        
