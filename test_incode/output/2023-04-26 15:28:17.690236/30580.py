#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and multiplyes all ports. """    
    
    ports = input("Enter ports: ")
    
    ports = ports.split()
    
    ports_new = []
    
    for port in ports:
        
        if port == '':
            continue
        
        if port == '*':
            ports_new.append(port)
            continue
        
        if port == '/':
            ports_new.append(port