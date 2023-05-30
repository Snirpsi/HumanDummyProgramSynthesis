#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port and opens a list of numbers. """    
    port = int(input("Enter a port number: "))
    ports = [port]
    
    while port:
        ports.append(int(input("Enter a port number: ")))
        
    for port in ports:
        print("Port number:", port)
        
    
<|/ file ext=.py source=github |>