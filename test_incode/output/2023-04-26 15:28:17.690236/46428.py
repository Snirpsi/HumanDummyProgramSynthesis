#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or enumerates all ports. """    
    import socket
    import sys
    
    HOST, PORT = "localhost", 8080
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while True:
        connection, client_address = sock.accept()
        print("Got connection from", client_address)
        
        connection.sendall("HTTP/1.1 200 OK\r\n")
        connection.sendall("Server: Apache\r\n")
        connection.sendall("Content-Type: text/html\r\n")
        connection.sendall("\r\n")
        
        connection.sendall("<html>\r\n")
        connection.sendall("<head>\r\n")
        connection.sendall("<title>Apache Ports</title>\r\n")
        connection.sendall("</head>\r\n")
        connection.sendall("<body>\r\n")
        connection.sendall("<h1>Apache Ports</h1>\r\n")
        connection.sendall("</body>\r\n")
        connection.sendall("</html>\r\n")
        
        connection.close()
        
