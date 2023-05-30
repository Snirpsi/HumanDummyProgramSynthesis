#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and enumerates words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', port))
    server.listen(1)
    
    while True:
        client, addr = server.accept()
        
        words = words + client.read().split()
        
        client.close()
    
    for word in words:
        print(word)
        
