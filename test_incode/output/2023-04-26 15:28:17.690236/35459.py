#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', port))
    sock.listen(5)
    
    while True:
        sock, addr = sock.accept()
        print("Got connection from", addr)
        
        sock.settimeout(10)
        
        buf = sock.recv(1024)
        
        if buf:
            print(buf)
            sock.sendall(buf)
        else:
            print("Connection closed by client")
            break
        
    sock.close()
    
