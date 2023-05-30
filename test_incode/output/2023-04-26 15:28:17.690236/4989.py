#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    print("Enumerating port %s" % port)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("Got connection from %s" % str(addr))
        
        conn.send("Hello from Python!")
        conn.close()
        
