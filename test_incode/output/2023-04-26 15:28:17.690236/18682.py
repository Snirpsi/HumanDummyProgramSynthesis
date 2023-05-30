#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    client, address = sock.accept()
    
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        client.send(data)
    
    client.close()
    
    sock.close()
    
