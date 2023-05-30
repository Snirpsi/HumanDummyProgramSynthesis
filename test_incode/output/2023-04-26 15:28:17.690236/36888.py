#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import socket
    
    HOST, PORT = "localhost", 9999
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("Got connection from", addr)
        
        conn.send(b"GET / HTTP/1.0\r\n\r\n")
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
            
            conn.send(b"Content-Type: text/plain\r\n\r\n")
            conn.send(data)
            
            conn.send(b"\r\n\r\n")
            
        conn.close()
        
    sock.close()
    
