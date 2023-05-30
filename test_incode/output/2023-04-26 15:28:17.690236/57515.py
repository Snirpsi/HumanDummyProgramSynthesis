#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and enumerates all ports. """    
    import sys
    import socket
    
    words = ['word1', 'word2', 'word3']
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 0))
    server_socket.listen(5)
    
    while True:
        connection, client_address = server_socket.accept()
        
        print('Client connected:', client_address)
        
        for word in words:
            connection.send(word)
            
        connection.close()
    
    server_socket.close()
    
    print('Server shut down')
    
