#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and converts a port. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', 'is', 'it', 'ok']
    
    words2port = {word: port for word in words}
    
    port2words = {port: word for word in words}
    
    words2port2 = {word: port for word in words2port}
    
    port2words2 = {port: word for word in port2words}
    
    print('\n'.join(port2words2[port] for port in port2words))
    
