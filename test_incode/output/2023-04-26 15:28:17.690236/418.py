#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    
    port = int(sys.argv[1])
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    
    client, address = server.accept()
    
    print('Connected by', address)
    
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        client.sendall(data)
    
    client.close()
    server.close()
    
