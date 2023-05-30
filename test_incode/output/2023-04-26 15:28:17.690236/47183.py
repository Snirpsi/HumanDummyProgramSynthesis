#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    
    while True:
        connection, client_address = server_socket.accept()
        
        print('Got connection from ', client_address)
        
        connection.sendall(b'Hello, world!\n')
        
        connection.close()
        
