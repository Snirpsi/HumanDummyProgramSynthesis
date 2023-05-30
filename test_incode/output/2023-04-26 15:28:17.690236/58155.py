#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words or multiplyes all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print('Usage: python add_words_to_ports.py <ports>')
        exit(1)
    
    for port in ports:
        add_words_to_ports(port)
    
