#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    client, addr = sock.accept()
    
    while True:
        data = client.recv(1024)
        if not data: break
        
        sys.stdout.write(data)
        sys.stdout.flush()
        
        client.send(b'OK')
        
    sock.close()
    
    client.close()
    
