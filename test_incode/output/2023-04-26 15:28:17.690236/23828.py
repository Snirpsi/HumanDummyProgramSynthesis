#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    
    while True:
        
        ports = listen_socket.getsockname()
        
        for port in ports:
            
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('', port))
            server_socket.listen(1)
            
            print('Server listening on port 