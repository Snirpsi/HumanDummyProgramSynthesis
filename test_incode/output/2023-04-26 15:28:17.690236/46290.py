#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and iterates over a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen(1)
    
    while True:
        client, address = server.accept()
        
        words.append(client.recv(1024).decode())
        
        client.close()
        
        print(' '.join(words))
        
        words = []
        
        server.close()
    
