#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and opens a list of words. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    words = [word for port in ports for word in words_in_port(port)]
    
    print('\n'.join(words))
    
