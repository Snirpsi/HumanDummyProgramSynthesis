#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        print("Got connection from %s" % str(addr))
        
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            client.send(data)
        
        sock.close()
        
        client.close()
        
