#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from %s' % client_address)
        
        while True:
            data = connection.recv(1024)
            if not data:
                break
            
            connection.sendall(data)
            
        connection.close()
