#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or enumerates a list of words. """    
    ports = []
    words = []
    
    # Open all ports
    for port in range(0, 65535):
        ports.append(port)
    
    # Open all words and print their ports
    for word in words:
        ports.append(word.port)
        
    # Print the ports
    for port in ports:
        print('Port {} is open'.format(port))
        
    # Print the words
    for word in words:
        print('Port {} is open'.format(word.port))
        
    # Close all ports
    for port in ports:
        sock.close()
    
    # Close all words
    for word in words:
        sock.close()
        
