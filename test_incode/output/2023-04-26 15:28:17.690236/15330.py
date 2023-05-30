#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports and stores numbers. """    
    ports = []
    
    ports.append( ('tcp', 80, 80) )
    ports.append( ('tcp', 443, 443) )
    ports.append( ('tcp', 8080, 8080) )
    
    for port in ports:
        print(port)
        
