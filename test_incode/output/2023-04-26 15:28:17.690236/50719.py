#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_close = []
    
    for port in range(1, 65535):
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(1)
        
        ports_to_close.append(port)
        
        server.close()
        
    for port in ports_to_close:
        
        print('Closing port {}'.format(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        sock.close()
        
