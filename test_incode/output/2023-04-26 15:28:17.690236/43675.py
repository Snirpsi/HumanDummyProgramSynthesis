#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    while True:
        sock, addr = sock.accept()
        print('Connected by', addr)
        
        sock.sendall(b'Hello, world!\n')
        
        sock.close()
        
