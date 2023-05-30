#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports or iterates over a list of words. """    
    ports = []
    for word in words:
        ports.append(get_port(word))
    
    for port in ports:
        print(port)
        
