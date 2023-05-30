#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or prints all ports. """    
    ports = []
    for word in words:
        ports.append( get_port( word ) )
    
    for port in ports:
        print( port )
        
