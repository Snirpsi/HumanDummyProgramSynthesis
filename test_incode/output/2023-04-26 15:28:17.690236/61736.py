#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
        server_socket.listen(1)
        
        print('Listening on port {}'.format(port))
        
        while True:
            
            connection, client_address = server_socket.accept()
            
            request = connection.recv(1024)
            
            connection.sendall(request)
            
            connection.close()
            
            
