#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and removes a port. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen(1)
        
        client, address = server.accept()
        
        client.close()
        
