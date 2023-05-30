#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and adds a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    # Open a socket and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept a connection and receive the data
    conn, addr = sock.accept()
    
    # Receive the data
    data = conn.recv(1024)
    
    # Send the data
    conn.send(b'HTTP/1.1 200 OK\r\nServer: Werkzeug\r\nContent-Type: text/plain\r\n\r\n' + data + b'\r\n\r\n')
    
    # Close the connection
    conn.close()
    
    # Print the data
    print(data)
    
    # Close the socket
    sock.close()
    
    # Print the port
    print(port)
    
    # Print the words
    for word in words:
        print(word)
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.close()
    
    # Close the program
    