#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    client, addr = sock.accept()
    
    while True:
        data = client.recv(1024)
        if not data: break
        
        client.send(data)
        
    sock.close()
    
