#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from %s:%d' % (client_address[0], client_address[1]))
        
        words = connection.