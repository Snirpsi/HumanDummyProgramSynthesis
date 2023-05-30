#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or prints fruits. """    
    port = int(sys.argv[1])
    
    # Create a socket and bind it to port 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8000))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection and print its content
    conn, addr = sock.accept()
    
    # Receive the request and print it back
    data = conn.recv(1024)
    print(data)
    
    # Close the connection
    conn.close()
    
    # Close the socket
    sock.close()
    
