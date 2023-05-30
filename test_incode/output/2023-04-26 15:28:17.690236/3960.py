#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and prints all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    print("Enumerating port %s" % port)
    
    import socket
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.bind(('', port))
    
    print("Listening on port %s" % port)
    
    s.listen(1)
    
    while True:
        conn, addr = s.accept()
        print("Got connection from %s" % addr)
        
        conn.send("HTTP/1.1 200 OK\r\nServer: WebServer\r\nConnection: close\r\n\r\nHello from WebServer")
        
        conn.close()
        
