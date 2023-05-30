#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_close = []
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 0))
    server_socket.listen(5)
    
    while True:
        connection, client_address = server_socket.accept()
        
        ports_to_close.append(connection)
        
        connection.close()
        
        for port in ports_to_close:
            port.close()
            
        ports_to_close = []
        
