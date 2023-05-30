#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and enumerates a port. """    
    
    ports = []
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        ports.append(connection)
        
        connection.send('HTTP/1.1 200 OK\r\n\r\n