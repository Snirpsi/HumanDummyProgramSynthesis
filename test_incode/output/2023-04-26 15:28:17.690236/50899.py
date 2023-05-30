#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and iterates over all ports. """    
    
    ports = []
    
    while True:
        ports.append(input('Enter a port number: '))
        
        if ports[-1] == 'stop':
            break
        
        print('Port number:', ports[-1])
        
    
    for port in ports:
        print('Printing words for port', port)
        
        words = 