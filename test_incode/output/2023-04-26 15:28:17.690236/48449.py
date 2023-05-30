#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or prints fruits. """    
    
    import os
    import socket
    import sys
    
    HOST, PORT = "localhost", 8000
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("Connected by", addr)
        
        data = conn.recv(1024)
        
        if not data:
            break
        
        conn.sendall("HTTP/1.1 200 OK\r\n")
        conn.sendall("Content-Type: text/html\r\n")
        conn.sendall("\r\n")
        conn.sendall("<html><body>")
        conn.sendall("<h1>")
        conn.sendall(data)
        conn.sendall("</h1>")
        conn.sendall("</body></html>\r\n")
        conn.close()
        
    sock.close()

<|/ file source=github filename=server.py |>