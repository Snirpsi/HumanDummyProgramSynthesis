#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that removes a port.
    def del_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", port))
        sock.listen(1)
        sock.close()
    
    #A function that opens a port and listens for connections.
    def open_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", port))
        sock.listen(1)
        sock.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection(sock):
        connection, address = sock.accept()
        connection.sendall("GET / HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection2(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection3(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection4(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection5(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection6(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection7(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection8(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection9(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection10(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection11(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection12(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection13(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection14(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection15(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection16(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection17(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection18(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection19(sock):
        connection, address = sock.accept()
        connection.sendall("GET /index.html HTTP/1.0\r\n\r\n")
        connection.close()
    
    #A function that accepts a connection and prints its contents.
    def accept_connection20(sock):
        