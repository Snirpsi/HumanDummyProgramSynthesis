#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port and opens a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Opening port %d" % port)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("Connected by", addr)
        conn.send(b"Hello, world")
        conn.close()
    
