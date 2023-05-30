#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and opens a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        print("Connected by", addr)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(buf)
        
        buf = client.recv(1024)
        if not buf:
            print("Disconnected")
            break
        
        client.send(