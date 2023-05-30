#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port and opens a port. """    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    client, addr = server_socket.accept()
    
    