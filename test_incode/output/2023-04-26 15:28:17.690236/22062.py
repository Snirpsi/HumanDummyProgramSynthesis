#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    # Create a TCP socket and bind to port 5000.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 5000))
    
    # Start listening for connections.
    sock.listen(1)
    
    # Accept a connection and make a file-like object out of it.
    conn, addr = sock.accept()
    
    # Create a file-like object from the connection.
    stream = io.TextIOWrapper(conn, encoding='utf8')
    
    # Iterate over lines in the file-like object.
    for line in stream:
        print(line)
    
    # Close the connection.
    stream.close()
    
    # Close the socket.
    conn.close()
    
    # Close the socket.
    sock.close()
    
    # Close the socket.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
