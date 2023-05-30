#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        print('Connection from', client_address)
        
        connection.send(b'Hello, world!')
        
        connection.close()
